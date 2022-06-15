import bs4
import requests
import lxml
'''
base_url = "http://books.toscrape.com/catalogue/page-{n}.html"
re = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(re.text, 'lxml')
product = soup.select(".product_pod")
example = product[0]
print(example.select('.star-rating.Three'))
print(example.select('a')[1]['title'])
'''

two_star_books = []
base_url = "http://books.toscrape.com/catalogue/page-{}.html"
for n in range(1, 51):
    page = base_url.format(n)
    re = requests.get(page)
    soup = bs4.BeautifulSoup(re.text, "lxml")
    product = soup.select('.product_pod')

    for book in product:
        if "star-rating Two" in str(book):
            two_star_books.append(book.select('a')[1]['title'])

for b in range(0, len(two_star_books)):
  print(two_star_books[b])