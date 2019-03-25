import requests
from bs4 import BeautifulSoup
import re

# Nike Men's Size 12 Lebron 15's, brand new in box
url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=lebron+15&_sacat=15709&US%2520Shoe%2520Size%2520%2528Men%2527s%2529=12&_dcat=15709&rt=nc&LH_ItemCondition=1000"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

class product:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link
    def __str__(self):
        return "Name: %s\nPrice: %d\nLink: %s" % (self.name, self.price, self.link)
        

# Holds prices of products in URL
prices = soup.select(".s-item__price")

# Initiates empty list
priceList = [] 

# Goes through every item
for item in prices:
    text = item.text # Holds text for each item's price
    rest = text.split(' ', 1)[0] # Removes everything after first space
    rest = re.sub('[!@#$,]', '', rest) # Removes these symbols
    priceList.append(float(rest)) # appends prices as floats in list

# Sorts prices
priceList.sort()
print(priceList)


""" product1 = product("Product", 9.99, "www.youtube.com")
print(product1) """


