import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)

soup = BeautifulSoup(r.text,"html5lib")
for content in soup.find_all(class_="content-section"):
        for para in content.find_all('p'):
                for child in para.descendants:
                        print(child)
