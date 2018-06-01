from selenium import webdriver

#login no sistema financeiro

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
driver.find_element_by_name('username').send_keys('adm')
driver.find_element_by_name('password').send_keys('********')
#Login no sistema
driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input').click()

#Entra na aba financeiro
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/th/a').click()

#Clica em adicionar dados
driver.find_element_by_xpath('/html/body/div/div[3]/div/ul/li/a').click()

#ADICIONA DADOS
driver.find_element_by_name('titulo').send_keys('Aluguel')
driver.find_element_by_name('valor').send_keys('1054.23')
driver.find_element_by_name('_save').click()