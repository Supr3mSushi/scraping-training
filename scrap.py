from bs4 import BeautifulSoup
import requests
import pandas as pd
from elements import elements

baseUrl = 'https://www.decitre.fr'
ure = '/livres/nouveautes.html?p='
finalUrl = baseUrl + ure
pages = 30


def getSoupFromUrl(url):
    request = requests.get(url)
    return BeautifulSoup(request.text, 'html.parser')


def getBookInfo(soup):
    books = []
    bookList = soup.findAll('li', class_='fiche-produit')
    for book in bookList:
        title = book.find("a", class_="product-title").text.strip()
        autor = book.find("div", class_="authors").text.strip()
        price = book.find("div", class_="price-container").find("span", class_="final-price").contents[-1].text.strip()
        disponibility = book.find("div", class_="dct-product-availability").contents[0].text.strip()
        link = book.find("div", class_="catalog-product-list-image").find('a')["href"]
        books.append(elements(title, autor, price, disponibility, link))
    return books


def main():
    books = []
    for i in range(0, pages):
        soup = getSoupFromUrl(finalUrl + str(i))
        books += getBookInfo(soup)

    data = pd.DataFrame([book.__dict__ for book in books])
    data.to_csv("books.csv", sep='\t', encoding='utf-8', index=False)


main()
