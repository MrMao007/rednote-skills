import argparse
import json
import re
from playwright.sync_api import sync_playwright
import asyncio
from datetime import datetime

def dump_note(note_url: str) -> str:
    """
    导出小红书笔记内容
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try: 
            context = browser.new_context(storage_state="rednote_cookies.json")
        except FileNotFoundError:
            return "❌ 未找到 cookies 文件，请先登录小红书并保存 cookies"
        page = context.new_page()
        page.goto(note_url)
        print("🌐 导航到小红书笔记页面...")
        page.wait_for_timeout(1000)
        login_button = page.locator("form").get_by_role("button", name="登录")
        if(login_button.is_visible()):
            return "❌ 未登录小红书，请先登录"
        
        # 直接在浏览器端提取 note 字段
        note_data = page.evaluate("""
            () => {
                const noteDetailMap = window.__INITIAL_STATE__?.note?.noteDetailMap;
                if (noteDetailMap) {
                    const firstKey = Object.keys(noteDetailMap)[0];
                    return JSON.stringify(noteDetailMap[firstKey]?.note);
                }
                return null;
            }
        """)
        json_data = json.loads(note_data)
        markdown_content = generate_rednote_markdown(json_data)

        context.close()
        browser.close()
            
        return markdown_content
    
def generate_rednote_markdown(json_data):
    # 提取数据
    note_type = json_data['type']
    title = json_data['title']
    desc = json_data['desc']
    nickname = json_data['user']['nickname']
    avatar = json_data['user']['avatar']
    tags = [tag['name'] for tag in json_data['tagList']]
    liked_count = json_data['interactInfo']['likedCount']
    collected_count = json_data['interactInfo']['collectedCount']
    comment_count = json_data['interactInfo']['commentCount']
    share_count = json_data['interactInfo']['shareCount']
    create_time = datetime.fromtimestamp(json_data['time']/1000)
    update_time = datetime.fromtimestamp(json_data['lastUpdateTime']/1000)
    images = [image['urlDefault'] for image in json_data['imageList']] if 'imageList' in json_data else []
    video_url = json_data['video']['media']['stream']['h264'][0]['masterUrl'] if 'video' in json_data else None
    ip_location = json_data.get('ipLocation', '')
    
    # 生成 Markdown
    markdown = f"""# {title}

<div align="center">
<img src="{avatar}" width="50" style="border-radius: 50%;" />

**{nickname}**
</div>

"""
    
    # 添加媒体内容
    if note_type == "video" and video_url:
        markdown += f"""## 🎬 视频

<div style="position: relative; width: 100%; padding-top: 56.25%;">
    <iframe 
        src="{video_url}" 
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
        scrolling="no" 
        border="0" 
        frameborder="no" 
        allowfullscreen="true">
    </iframe>
</div>

""" 
    if note_type == "normal" and images:
        markdown += """## 🖼️ 图片

"""
        for idx, img_url in enumerate(images, 1):
            markdown += f"![图片{idx}]({img_url})\n\n"
    
    # 添加互动数据
    markdown += f"""

## 📝 正文

{desc}

## 🏷️ 标签

{' '.join([f'`#{tag}`' for tag in tags])}

## 📊 互动数据

| 👍 点赞 | ⭐ 收藏 | 💬 评论 | 🔗 分享 |
|:---:|:---:|:---:|:---:|
| {liked_count} | {collected_count} | {comment_count} | {share_count} |

## ℹ️ 其他信息

- **发布时间**：{create_time.strftime('%Y-%m-%d %H:%M:%S')}
- **更新时间**：{update_time.strftime('%Y-%m-%d %H:%M:%S')}
- **IP 属地**：{ip_location}
- **内容类型**：{'📹 视频' if note_type == 'video' else '📷 图文'}
"""
    
    return markdown

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="导出小红书笔记内容")
    parser.add_argument("note_url", type=str, help="小红书笔记URL")
    args = parser.parse_args()
    note_url = args.note_url
    
    result = dump_note(note_url)
    print(result)