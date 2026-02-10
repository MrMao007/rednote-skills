import argparse
from playwright.sync_api import sync_playwright

def comment_note(note_url: str, comment_text: str) -> str:
    """
    评论小红书笔记
    :param note_url: 笔记URL
    :param comment_text: 评论内容
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
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
        
        page.locator(".chat-wrapper > .reds-icon").click()
        page.locator("#content-textarea").fill(comment_text)
        page.get_by_role("button", name="发送").click()
        
        context.close()
        browser.close()
        
            
        return "💬 评论已发布"

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="评论小红书笔记")
    parser.add_argument("note_url", type=str, help="小红书笔记URL")
    parser.add_argument("comment_text", type=str, help="评论内容")
    args = parser.parse_args()
    note_url = args.note_url
    comment_text = args.comment_text
    
    result = comment_note(note_url, comment_text)
    print(result)