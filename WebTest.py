from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/js/")
    page.wait_for_selector(".quote")

    quotes = page.query_selector_all(".quote")

    data = []

    for q in quotes[:5]:
        text = q.query_selector(".text").inner_text()
        author = q.query_selector(".author").inner_text()

        data.append((text, author))

    for i, (text, author) in enumerate(data, 1):
        print(f"{i}. {text} - {author}")

    browser.close()