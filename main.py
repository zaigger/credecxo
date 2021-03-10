from bs4 import BeautifulSoup
import requests

proxies = {
    "http": "http//188.0.138.11",
    "h": "http//117.245.139.4"
}

# requests.get("http://example.org", proxies=proxies)
page = requests.get("https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1", proxies=proxies)
soup = BeautifulSoup(page.content, 'html.parser')
list = []
products = soup.find_all(class_="product")
for prod in products:
    d = {}
    name = prod.find_all(class_="catalog-item-name")
    brand = prod.find_all(class_="catalog-item-brand")
    price = prod.find_all(class_="price")
    stock = prod.find_all(class_="out-of-stock")
    d['price'] = price[0].get_text()
    d['title'] = name[0].get_text()
    d['stock'] = stock[0].get_text()
    d['maftr'] = brand[0].get_text()
    list.append(d)

print(list)


