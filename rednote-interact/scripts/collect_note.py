from playwright.sync_api import sync_playwright

def collect_note(note_url: str) -> str:
    """
    收藏小红书笔记
    :param noteUrl: 笔记URL
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="src/rednote_mcp_plus/cookie/rednote_cookies.json")
        page = context.new_page()
        page.goto(note_url)
        print("🌐 导航到小红书笔记页面...")
        page.wait_for_timeout(1000)
        login_button = page.locator("form").get_by_role("button", name="登录")
        if(login_button.is_visible()):
            return "❌ 未登录小红书，请先登录"
        
        page.locator(".reds-icon.collect-icon").click()

        context.close()
        browser.close()
            
        return "📥 笔记已收藏"

if __name__ == "__main__":
    note_url = "https://www.xiaohongshu.com/explore/69650e49000000000b01327c?xsec_token=ABv2EGvoPK_6ildvjUhwB5MIhms8PhQyc0IBd4jaXbb1g=&xsec_source=pc_user"
    result = collect_note(note_url)
    print(result)