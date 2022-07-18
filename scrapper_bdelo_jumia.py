from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.jumia.co.ke/catalog/?q=bdelo"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('article', class_="prd _fb col c-prd")

with open('bdelo.csv','w', encoding='utf8', newline='') as file:
    bdelo_writer = writer(file)
    header = ['Name','Image','Price']
    bdelo_writer.writerow(header)
    for list in lists:
        name = list.find('h3', class_="name").text
        img = list.img['data-src']
        price = list.find('div', class_="prc").text

        data = [name, img, price]

        bdelo_writer.writerow(data)






