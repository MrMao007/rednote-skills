from html import parser
from playwright.sync_api import sync_playwright
import argparse


def search(key_word: str, top_n: int) -> list[str]:
    """
    搜索小红书笔记
    """
    with sync_playwright() as playwright:
        browser =playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state="rednote_cookies.json")
        page = context.new_page()
        page.goto("https://www.xiaohongshu.com/search_result?keyword=" + key_word)
        print("🌐 导航到小红书主页...")
        page.wait_for_timeout(3000)
        login_button = page.locator("form").get_by_role("button", name="登录")
        if(login_button.is_visible()):
            return ["❌ 未登录小红书，请先登录"]
        
        herfs = []
        prefix = 'https://www.xiaohongshu.com'
        links = page.query_selector_all('a.cover.mask.ld')
        # 获取所有 href 属性
        hrefs = []
        for link in links:
            href = link.get_attribute('href')
            if href:
                href = prefix + href
                hrefs.append(href)
            if len(hrefs) >= top_n:
                break
        markdown_content = []
        for href in hrefs:
            hrefs.append


        context.close()
        browser.close()
            
        return hrefs
            
        

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="搜索小红书笔记")
    parser.add_argument("keyword", type=str, help="搜索关键词")
    parser.add_argument("--top_n", type=int, default=5, help="返回的笔记数量")
    args = parser.parse_args()
    key_word = args.keyword
    top_n = args.top_n
    
    result = search(key_word, top_n)
    print(result)