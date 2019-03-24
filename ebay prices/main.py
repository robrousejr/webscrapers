import requests
from bs4 import BeautifulSoup

# Nike Men's Size 12 Lebron 15's
url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=lebron+15&_sacat=15709&US%2520Shoe%2520Size%2520%2528Men%2527s%2529=12&_dcat=15709&rt=nc&LH_ItemCondition=1000"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Holds prices of products in URL
prices = soup.select(".s-item__price")

# Goes through every item
for item in prices:
    print(item.text) # prints out text (price) of each item

