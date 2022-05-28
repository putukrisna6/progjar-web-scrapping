import requests
import sys
from bs4 import BeautifulSoup

def getGoPackage(query, n):
    page = requests.get("https://pkg.go.dev/search?limit=" + str(n) + "&m=package&q=" + query)
    soup = BeautifulSoup(page.content, 'html.parser')
    pkg_detail = soup.find("div", class_="SearchSnippet")
    print(pkg_detail)
    # link = pkg_detail.select('a', href=True)
    # print(link)
    # return desc
    # return num + ", akan mengambil: " + title

getGoPackage("sort", 10)
# print(getGoBlog(sys.argv[1]))