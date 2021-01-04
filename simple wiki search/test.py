from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get('https://www.amazon.in/ref=nav_logo')

#print(driver.title)

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys('car')
search.send_keys(Keys.RETURN)

#print(driver.page_source)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "mw-content-text"))
#     )
#     print(main.text)

#     #articles = main.find_element_by_tag_name('article')
#     #for artical in articles:
#     #	header = article.find_element_by_class_name('entry-title')
#     #	print(header.taxt)

# except:
#     driver.quit()

# time.sleep(5)

# driver.quit()
