import requests
from bs4 import BeautifulSoup

def scrape_amazon():
    url = "https://www.amazon.in/s?k=smartphones&rh=p_36%3A-2000000"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    results = soup.find_all("div", {"data-component-type": "s-search-result"})

    for result in results:
        title_element = result.find("span", {"class": "a-size-medium"})
        price_element = result.find("span", {"class": "a-price-whole"})

        if title_element and price_element:
            title = title_element.text.strip()
            price = price_element.text.strip()

            print("Phone Name:", title)
            print("Price:", price)
            print("---------------------")

scrape_amazon()

