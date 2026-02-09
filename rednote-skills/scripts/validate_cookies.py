from playwright.sync_api import sync_playwright


def validate_cookies() -> bool:
    """验证保存的cookies是否有效"""
    with sync_playwright() as playwright:
        browser =playwright.chromium.launch(headless=False)
        try: 
            context = browser.new_context(storage_state="rednote_cookies.json")
        except FileNotFoundError:
            return False
        page = context.new_page()
        page.goto("https://www.xiaohongshu.com/explore")
        
        # 检查是否登录成功
        login_button = page.locator("form").get_by_role("button", name="登录")
        is_login = not login_button.is_visible()
        
        context.close()
        browser.close()
        
        return is_login

if __name__ == "__main__":
    result = validate_cookies()
    print(result) 