import requests
from bs4 import BeautifulSoup

def scrape_amazon():
    url = "https://www.tripadvisor.in/"
    response = requests.get(url)
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


