from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
search = input("향수 이름: ")

target_url = baseUrl + quote_plus(search)
html = urlopen(target_url)
soup = bs(html, "html.parser")
img = soup.find_all(class_="_img")

n = 0
for i in img:
    imgUrl = i["data_source"]
    with urlopen(imgUrl) as f:
        with open('./img/' + search + '_' + str(n) +'.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n+=1
