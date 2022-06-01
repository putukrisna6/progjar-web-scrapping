import requests
import sys
from bs4 import BeautifulSoup

def getGoPackage(query, n):
    page = requests.get("https://pkg.go.dev/search?limit=" + str(n) + "&m=package&q=" + query)
    soup = BeautifulSoup(page.content, 'html.parser')
    for list_pkg in soup.findAll("div", class_="SearchSnippet"):
        print("https://pkg.go.dev" + list_pkg.find('a')['href'])
        if (list_pkg.find('p') == None):
            print("No description\n")
        else:
            print(list_pkg.find('p').text.strip()+"\n")

getGoPackage("sort", 10)
# print(getGoBlog(sys.argv[1]))