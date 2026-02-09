import argparse
from playwright.sync_api import sync_playwright

def follow_user(note_url: str) -> str:
    """
    关注小红书用户
    :param note_url: 笔记URL
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
        
        result = "👤 用户已关注"
        try:
            page.get_by_role("button", name="关注").click()
        except Exception as e:
            result = "⚠️ 已经关注该用户或无法关注"
            
        context.close()
        browser.close()

        return result

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="关注小红书用户")
    parser.add_argument("note_url", type=str, help="小红书笔记URL")
    args = parser.parse_args()
    note_url = args.note_url
    
    result = follow_user(note_url)
    print(result)