from playwright.sync_api import sync_playwright

def follow_user(note_url: str) -> str:
    """
    关注小红书用户
    :param note_url: 笔记URL
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state="src/rednote_mcp_plus/cookie/rednote_cookies.json")
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
    note_url = "https://www.xiaohongshu.com/explore/69650e49000000000b01327c?xsec_token=ABv2EGvoPK_6ildvjUhwB5MIhms8PhQyc0IBd4jaXbb1g=&xsec_source=pc_user"
    result = follow_user(note_url)
    print(result)