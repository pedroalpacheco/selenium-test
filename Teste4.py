from selenium import webdriver

#login no github

driver = webdriver.Firefox()
driver.get("https://github.com/login")
driver.find_element_by_name('login').send_keys('xxxxxx@gmail.com')
driver.find_element_by_name('password').send_keys('SSSSSSSSSSSS')
driver.find_element_by_name('commit').click()