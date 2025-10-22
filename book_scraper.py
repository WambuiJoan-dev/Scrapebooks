import requests
from bs4 import BeautifulSoup

#target url to scrape
url = "https://books.toscrape.com/"

#send http request to the url
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
#soup- a parsed, tree-like representation of the page that you can search easily
#html.parser-turns plain html text into a navigable structure

#find all product containers.Searches soup for every html element that is an <article> tag and has a css class product___pod
books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["tiitle"]#book.h3 finds the first <h3> tag inside the book element, .a fins the first <a> tag inside h3
    price = book.find("p", class_="price_color").text #extract text
    print(f"{title}-{price}")

