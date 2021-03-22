import requests
from bs4 import BeautifulSoup
"""
딥디크
조말론,
바이레도,
르라보,
아쿠아 디 파르마,
톰포드,
산타마리아노벨라,
크리드,
세르주루텐,
아닉구딸,
펜할리곤스,
메종,
랑세
"""

jomalone = "https://www.jomalone.co.kr/product/3568/10101/s/lime-basil-mandarin-cologne"

res_jomalone = requests.get(jomalone)
# print(res_jomalone.content)
# print(res_jomalone.encoding)

html_jomalone = res_jomalone.content.decode('utf-8').strip('\n')

# print(html_jomalone)

soup_jomalone = BeautifulSoup(html_jomalone, "html.parser")
text = soup_jomalone.select_one('#node-20242 > div > div > div > ul > li:nth-child(3) > div > div > div > div > div > div > div')
name = text.select("ul>li>ul>li>a")
jomalone_name = [n.get_text() for n in name]
print(jomalone_name)
print(len(jomalone_name))

with open("jomalone_product.txt",'w', encoding="utf-8") as f:
    for name in jomalone_name:
        f.write(name+'\n')


