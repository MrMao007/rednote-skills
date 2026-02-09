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
    note_url = "https://www.xiaohongshu.com/explore/69650e49000000000b01327c?xsec_token=ABv2EGvoPK_6ildvjUhwB5MIhms8PhQyc0IBd4jaXbb1g=&xsec_source=pc_user"
    result = like_note(note_url)
    print(result)