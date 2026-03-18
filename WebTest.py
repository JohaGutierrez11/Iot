from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #Si quiere que se muestre o no el navegador
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    #navega en la pagina
    page.goto("https://quotes.toscrape.com/js/")
    #busca el selector
    page.wait_for_selector(".quote")

    quotes = page.query_selector_all(".quote")

    data = []

    #muestra los textos y loa autores
    for q in quotes[:5]:
        text = q.query_selector(".text").inner_text()
        author = q.query_selector(".author").inner_text()

        data.append((text, author))

    for i, (text, author) in enumerate(data, 1):
        print(f"{i}. {text} - {author}")

    browser.close()