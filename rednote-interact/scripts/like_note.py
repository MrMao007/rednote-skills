import argparse
from playwright.sync_api import sync_playwright

def like_note(note_url: str) -> str:
    """
    点赞小红书笔记
    :param note_url: 笔记URL
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="rednote_cookies.json")
        page = context.new_page()
        page.goto(note_url)
        print("🌐 导航到小红书笔记页面...")
        page.wait_for_timeout(1000)
        login_button = page.locator("form").get_by_role("button", name="登录")
        if(login_button.is_visible()):
            return "❌ 未登录小红书，请先登录"
        
        page.locator(".left > .like-wrapper > .like-lottie").click()

        context.close()
        browser.close()
            
        return "❤️ 笔记已点赞"

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="点赞小红书笔记")
    parser.add_argument("note_url", type=str, help="小红书笔记URL")
    args = parser.parse_args()
    note_url = args.note_url
    
    result = like_note(note_url)
    print(result)