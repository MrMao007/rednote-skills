import os
from playwright.sync_api import sync_playwright

def save_cookies(context):
    """异步保存cookies到文件"""
    try:
        print("🍪 获取cookies...")
        os.makedirs("src/rednote_mcp_plus/cookie", exist_ok=True)  # 确保目录存在
        cookies_file = "rednote_cookies.json"
        storage_state = context.storage_state(path=cookies_file)
        
        print(f"✅ Cookies已保存到: {cookies_file}")
        print(f"📊 共保存了 {len(storage_state)} 个cookies")
    except Exception as e:
        print(f"保存cookies结束")

def manual_login() -> str:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        
        # 监听context关闭事件
        context.on("close", lambda: save_cookies(context)) # type: ignore
        
        page = context.new_page()
        print("🌐 导航到小红书登录页面...")
        page.goto("https://www.xiaohongshu.com/explore")
        
        print("\n📋 请按照以下步骤操作:")
        print("1. 在浏览器中手动登录小红书")
        print("2. 登录成功后，确保可以正常访问小红书内容")
        print("3. 完成后，关闭浏览器...")
        
        try:
            # 无限等待，直到页面被关闭
            page.wait_for_event("close", timeout=0)
        except Exception as e:
            print(f"等待过程中断: {e}")
        finally:
            save_cookies(context)
            browser.close()
        
        return "✅ 登录流程完成，Cookies已保存"

if __name__ == "__main__":
    result = manual_login()
    print(result)