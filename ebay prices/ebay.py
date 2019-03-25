from script import *

"""
File meant for ebay functions, allows us to ask user for search query and conditions, 
and build a list based off of this information

eBay URL Parameters:
http://www.helios825.org/url-parameters.php

In order
-----------------------------------------------
start of URL = https://www.ebay.com/sch/i.html?
keyword = &_nkw=Starbucks%20card : keyword
&_ipg=200 : Items Per Page (200,100,50,25,10,5)
&_sop=15 : Price + Shipping: Lowest First
&LH_ItemCondition=1000 : condition = Brand New
""" 

# Creates keyword param for URLmaker
def getKeyword():
    keywordInput = input("Type in keyword: ")
    # Verfifies keyword is > 1 character
    while len(keywordInput) < 2:
        keywordInput = input("Type in keyword (more than 1 character): ")
    keywordInput = keywordInput.strip() # Removes unneeded spaces
    keywordInput = keywordInput.replace(" ", "%20") # Makes string work for ebay search
    return keywordInput
    
# Returns string based off of if they want new/used/all products 
def newOrUsed():
    newOrUsed = ""
    # Verifies they use one of the 3 strings
    while newOrUsed not in ['new', 'used', 'all']:
        newOrUsed = input("New, used, or all? ")
    newOrUsed = newOrUsed.strip() # Gets rid of all spaces before/after text
    newOrUsed = newOrUsed.lower() # converts to lowercase
    if newOrUsed == "new":
        return "11"
    if newOrUsed == "used":
        return "12"
    else:
        return "1000"
    
# Creates URL to return
def urlMaker():
    finalURL = "https://www.ebay.com/sch/i.html?"
    keyword = "&_nkw=" + getKeyword()
    itemsPerPage = "&_ipg=100"
    ascending = "&_sop=15"
    newUsedAll = "&LH_ItemCondition=" + newOrUsed()
    finalURL += keyword + itemsPerPage + ascending + newUsedAll # Combines all into one URL
    return finalURL
