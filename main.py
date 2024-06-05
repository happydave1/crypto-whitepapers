import requests
from bs4 import BeautifulSoup
import os

def get_top_cryptocurrencies(n=5):

    # get the html content of coinmarketcap.com, which shows the top cryptocurrencies
    url = "https://coinmarketcap.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    # TESTING: print out the html content of response (which should be html of the website)
    print(response.text) #works!

get_top_cryptocurrencies(0)