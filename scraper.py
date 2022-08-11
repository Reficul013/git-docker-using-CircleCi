from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")

print(doc.prettify)
