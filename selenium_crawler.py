import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
import time

URL = "https://www.fragrantica.com/perfume/Jo-Malone-London/Wood-Sage-Sea-Salt-25529.html"
driver = webdriver.Chrome(executable_path=r"C:\Users\rswfa\Documents\capstone2\Catchinichi-AI\chromedriver")
driver.get(url=URL)
print(driver.current_url)
driver.implicitly_wait(time_to_wait=5)
driver.execute_script("window.scrollTo(0, 1500)") 

# notes_page = driver.find_element_by_css_selector('#pyramid > div.cell > div > div > div > div > div > div > a')
notes = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[5]/div/div[1]/div/div[2]/div[3]/div').find_elements_by_css_selector("div > div > div")
# print(notes_page.text)
for note in notes:
    print(note.text)
# notes = driver.find_elements_by_css_selector('#pyramid > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(2)')
# print(notes)

driver.close()

# options = webdriver.ChromeOptions()
# options.add_argument('window-size=1920,1080')

# driver = webdriver.Chrome('chromedriver', options=options)
# driver.implicitly_wait(5)

# driver.get(url='https://www.google.com/')

# search_box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

# search_box.send_keys('greeksharifa.github.io')
# search_box.send_keys(Keys.RETURN)

# posting = driver.find_element_by_xpath('//*[@id="rso"]/div/div[1]/div/div/div[1]/a/h3')
# posting.click()

# time.sleep(3)
# driver.close()