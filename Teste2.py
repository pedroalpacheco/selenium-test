from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.camarablu.sc.gov.br/")
#assert "Furb" in driver.title
elem = driver.find_element_by_name("s")
elem.clear()
elem.send_keys("informatica")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()