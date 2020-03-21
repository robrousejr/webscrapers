from ebay import *
from script import *

# Holds URL based off of input
link = urlMaker()
list = makeList(link)
printList(list)

# Print list of prices
for product in list:
    print(product.price)