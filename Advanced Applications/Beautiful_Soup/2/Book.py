import requests
from bs4 import BeautifulSoup
import csv
import os
url = "http://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('h3')

prices = soup.find_all('p', {'class':'price_color'})

print('-'*30)
    
with open('books_data.csv','w',newline='',encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Book Name','Price'])


    for i in range(len(books)):
        price = prices[i].text.replace('Â', '').strip()
        book = books[i].text
        print(f"{book} -> {price}")
        writer.writerow([book, price])


os.startfile(r'D:\Work\Elzero\Python\Lib\Beautiful_Soup\2\books_data.csv')








