import requests
from bs4 import BeautifulSoup

def craw(max_page):
    page = 1
    while page <= max_page:
        url = "http://www.jikexueyuan.com/course/?pageNum=" + str(page)
        plainText = requests.get(url).text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll('a',{'target': '_blank', 'jktag': ''}):
            courseLink = link.get('href')
            print(courseLink)
        page += 1

if __name__ == "__main__":
    craw(1)