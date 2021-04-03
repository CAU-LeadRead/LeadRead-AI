import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
import time

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


def get_notes(URL):
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\rswfa\Documents\capstone2\Catchinichi-AI\chromedriver"
    )

    driver.get(url=URL)
    print(driver.current_url)
    driver.implicitly_wait(time_to_wait=5)
    driver.execute_script("window.scrollTo(0, 1500)")

    # notes = driver.find_elements_by_css_selector(
    #     "#pyramid > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(3) > div"
    # )

    notes = driver.find_elements_by_css_selector(
        "#pyramid > div:nth-child(1) > div > div:nth-child(2)"
    )

    for note in notes:
        print(note.text)

    driver.close()
    return notes


def main():
    res_jomalone = requests.get(jomalone)
    # print(res_jomalone.content)
    # print(res_jomalone.encoding)

    html_jomalone = res_jomalone.content.decode("utf-8").strip("\n")

    # print(html_jomalone)

    soup_jomalone = BeautifulSoup(html_jomalone, "html.parser")
    text = soup_jomalone.select_one(
        "#node-20242 > div > div > div > ul > li:nth-child(3) > div > div > div > div > div > div > div"
    )
    name = text.select("ul>li>ul>li>a")
    jomalone_name = [n.get_text() for n in name]
    # print(jomalone_name)
    # print(len(jomalone_name))


with open("jomalone_product.txt", "w", encoding="utf-8") as f:
    for name in jomalone_name:
        f.write(name + "\n")
