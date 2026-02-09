from playwright.sync_api import sync_playwright

def comment_note(note_url: str, comment_text: str) -> str:
    """
    评论小红书笔记
    :param note_url: 笔记URL
    :param comment_text: 评论内容
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
        
        page.locator(".chat-wrapper > .reds-icon").click()
        page.locator("#content-textarea").fill(comment_text)
        page.get_by_role("button", name="发送").click()

        context.close()
        browser.close()
            
        return "💬 评论已发布"

if __name__ == "__main__":
    note_url = "https://www.xiaohongshu.com/explore/69650e49000000000b01327c?xsec_token=ABv2EGvoPK_6ildvjUhwB5MIhms8PhQyc0IBd4jaXbb1g=&xsec_source=pc_user"
    result = comment_note(note_url, "赞！")
    print(result)