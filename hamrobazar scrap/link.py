from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()
driver.get('https://hamrobazaar.com/c28-computer-and-peripherals-graphic-and-video-cards')

#print(driver.page_source) 
item = ()
f = open('hamro.txt', 'a')
follow_loop = range(3, 23)

for x in follow_loop:
    xpath = "/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table["
    xpath += str(x)
    xpath += "]"
    item = driver.find_element_by_xpath(xpath)
    
    f.write(item.text+'\n')



link = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table[23]/tbody/tr/td/a/b/u')
link.click()
time.sleep(10)


while True:
	try:
		
		link = driver.find_element_by_xpath('html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table[23]/tbody/tr/td/a[2]')
		for x in follow_loop:
		    xpath = "/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table["
		    xpath += str(x)
		    xpath += "]"
		    item = driver.find_element_by_xpath(xpath)
		    
		    f.write(item.text+'\n')
		
		link.click()
		time.sleep(10)


	except NoSuchElementException:
		driver.quit()

# link = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table[23]/tbody/tr/td/a/b/u')
# if link==
# link.click()

# if:
# 	link = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table[23]/tbody/tr/td/a/b/u")
# 	print(link.text)

#selenium.common.exceptions.NoSuchElementException

