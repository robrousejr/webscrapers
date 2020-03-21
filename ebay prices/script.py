from ebay import * 
import requests
from bs4 import BeautifulSoup
import re

class product:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link
    def __str__(self):
        return "Name: %s\nPrice: $%d\nLink: %s\n" % (self.name, self.price, self.link)

"""
Returns list of information about product on eBay (names, price, link)
list[0] = name list
list[1] = price list
list[2] = link list
"""
def makeList(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Holds prices of products in URL
    prices = soup.select(".s-item__price")
    names = soup.select(".s-item__title")
    links = soup.select(".s-item__link", href=True)
    # Initiates empty list
    priceList = [] 
    nameList = []
    linkList = []

    # Goes through every item's price
    for item in prices:
        text = item.text # Holds text for each item's price
        rest = text.split(' ', 1)[0] # Removes everything after first space
        rest = re.sub('[!@#$,]', '', rest) # Removes these symbols
        priceList.append(float(rest)) # appends prices as floats in list

    # Goes through each item's name
    for p in names:
        nameText = p.text # Holds text for each item's name
        nameList.append(nameText) # Appends name text into nameList

    # Goes through each item's link
    for a in links:
        linkList.append(a['href']) # Appends link text into linkList
    
    sizeLists = len(priceList) # Holds number of elements in all 3 lists
    productList = [] # Will hold all final objects

    # Goes through each list and makes Product objects for each
    for prod in range(sizeLists):
        tmpProduct = product(nameList[prod], priceList[prod], linkList[prod])
        productList.append(tmpProduct)
    
    """ 
    To sort product list by price ascending:
    productList.sort(key=lambda x: x.price, reverse=False) 
    """
    return productList

# Prints out the contents of a list
def printList(prodList):
    assert(type(prodList) is list)
    for x in range(len(prodList)):
        print(prodList[x])

