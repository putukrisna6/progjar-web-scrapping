import requests
import sys
from bs4 import BeautifulSoup

def getGoBlog(num):
    page = requests.get("https://go.dev/doc/")
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.select("h3")[int(num)].string
    return num + ", akan mengambil: " + title

print(getGoBlog(sys.argv[1]))