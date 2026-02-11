import argparse
import re
from typing import List
from playwright.sync_api import sync_playwright

class RednoteArticle:
    def __init__(self, title: str, content: str, tags: List[str], image_urls: List[str]):
        self.title = title
        self.content = content
        self.tags = tags
        self.image_urls = image_urls

    def __str__(self):
        return f"标题: {self.title}, 内容: {self.content}, 标签: {', '.join(self.tags)}, 图片: {', '.join(self.image_urls)}"

    def __repr__(self):
        return self.__str__()


def publish_text(image_urls: List[str], title: str, content: str, tags: List[str]) -> str:
    """
    发布小红书图文笔记
    :param image_urls: 图片URL列表
    :param title: 笔记标题
    :param content: 笔记内容
    :param tags: 标签列表
    """
    rednoteArticle = RednoteArticle(title, content, tags, image_urls)
    
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try: 
            context = browser.new_context(storage_state="rednote_cookies.json")
        except FileNotFoundError:
            return "❌ 未找到 cookies 文件，请先登录小红书并保存 cookies"
        page = context.new_page()
        page.goto("https://www.xiaohongshu.com/explore")
        print("🌐 导航到小红书主页...")
        page.wait_for_timeout(10000)
        login_button = page.locator("form").get_by_role("button", name="登录")
        if(login_button.is_visible()):
            return "❌ 未登录小红书，请先登录"
        
        page.get_by_role("button", name="创作中心").hover()
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="创作服务").click()
            
        page1 = page1_info.value
        print("🕒 等待页面跳转")
        
        page1.get_by_text("发布图文笔记").click()
    
        
        print("🖼️ 上传图片...")
        page1.on("filechooser", lambda file_chooser: file_chooser.set_files(rednoteArticle.image_urls)) # 替换为你的文件路径
        
        page1.get_by_role("textbox", name="填写标题会有更多赞哦").fill(rednoteArticle.title)
        final_content = rednoteArticle.content + "\n\n" + "\n".join([f"#{tag}" for tag in rednoteArticle.tags])
        page1.get_by_role("paragraph").filter(has_text=re.compile(r"^$")).fill(final_content)
        page1.wait_for_timeout(10000) # 等待发布内容加载完成
        page1.get_by_role("button", name="发布").click()
        print("🕒 等待发布成功")
        page1.wait_for_timeout(5000) # 等待发布完成
        print("✅ 发布成功")
        
        # ---------------------
        context.close()
        browser.close()
        
        return "✅ 笔记发布成功"

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="发布小红书图文笔记")
    parser.add_argument("--image-urls", nargs="+", type=str, required=True, help="图片URL列表")
    parser.add_argument("--title", type=str, required=True, help="笔记标题")
    parser.add_argument("--content", type=str, required=True, help="笔记内容")
    parser.add_argument("--tags", nargs="+", type=str, required=True, help="标签列表")
    args = parser.parse_args()
    
    result = publish_text(args.image_urls, args.title, args.content, args.tags)
    print(result)