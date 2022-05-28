import requests
import sys
from bs4 import BeautifulSoup

def getGoPackage(query):
    #Request halaman pencarian
    page1 = requests.get("https://pkg.go.dev/search?q=" + query)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    link = soup1.find_all('a', attrs={"data-gtmc":"search result"}, href=True)[0]
    #Request link teratas
    page2 = requests.get("https://pkg.go.dev" + link['href'])
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    get_index_list = soup2.find('ul', class_="Documentation-indexList")
    get_link = get_index_list.find_all('a', href=True)
    for value in get_link:
        print(value.get_text())
    # print(test2)

getGoPackage((sys.argv[1]))