import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

url = 'https://rozetka.com.ua/ua/duracell_5003094/p109680888/'

headers = {'user-agent': fake_useragent.UserAgent().random}
#print(headers)
respons = requests.get(url, headers=headers)
#print(respons.status_code)
#print(respons.text)

soup= BeautifulSoup(respons.text, 'lxml')
#(soup)
products = soup.find_all('ul',calss_='catalog-grid ng-star-inserted')
#print(products)
for product in products:
    title_product = product.find('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
    print(title_product.text)