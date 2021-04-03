import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
import time

URL = "https://www.fragrantica.com/perfume/Jo-Malone-London/154-Cologne-17819.html"
URL = (
    "https://www.fragrantica.com/perfume/Jo-Malone-London/Wood-Sage-Sea-Salt-25529.html"
)

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