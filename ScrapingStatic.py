import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    print("Frases encontradas:\n")

    for i in range(len(quotes)):
        print(f"{i+1}. {quotes[i].text}")
        print(f"   Autor: {authors[i].text}\n")

else:
    print("Error al acceder a la página")