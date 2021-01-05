from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

driver = webdriver.Firefox()
#driver.get('https://www.daraz.com.np/')
driver.get('https://www.daraz.com.np/catalog/?q=dell&_keyori=ss&from=input&spm=a2a0e.pdp.search.go.70777cf6YQH5UR')

csv_file = open('daraz.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SN','Title','Price'])

#driver.execute_script("window.scrollTo(0, 8000)") 

# next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "aant-pagination-item-link")))
# #next_button.location_once_scrolled_into_view
# next_button.click()

# l = driver.find_element_by_class_name("ant-pagination-next")
# l.click()

while True:

	try:
		
		add = driver.find_elements_by_class_name('c2prKC')
		i= 1


		for x in add:
			title = x.find_element_by_class_name('c16H9d').text
			#print(title.text)

			price = x.find_element_by_class_name('c3gUW0').text

			csv_writer.writerow([i,title,price])
			i=i+1



		driver.find_element_by_class_name(" ant-pagination-next").click()
		print(link)
		link.click()
		#time.sleep(5)

	except NoSuchElementException:
		driver.quit()


csv_file.close()
driver.quit()

