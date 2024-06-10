import requests
from bs4 import BeautifulSoup
import os

def get_top_cryptocurrencies(n=5):

    # get the html content of coinmarketcap.com, which shows the top cryptocurrencies
    url = "https://coinmarketcap.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    cryptos = []
    rows = soup.select('table.sc-ae0cff98-3.ipWPGi.cmc-table tbody tr')
    for i, row in enumerate(rows[:n]):
        tds = row.select('td')
        name_td = tds[2]
        divs = name_td.select('div')
        name_div = divs[3]
        ps = name_div.select('p')
        name_p = ps[0]
        cryptocurrency_name = name_p.text
        cryptos.append(cryptocurrency_name)
        print("got " + cryptocurrency_name)
    
    return cryptos
    

print(get_top_cryptocurrencies(90))