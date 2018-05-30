from selenium import webdriver
import time

inicio = time.time() #mede tempo de execução

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'lst-ib' # id
        self.btn_search = 'btnK' # Name
        self.btn_lucky = 'btnI' # name

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_search).click()

    def lucky(self, word='None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_lucky).click()


ff = webdriver.Firefox()
g = Google(ff)
g.navigate()

g.search('Pedro')
ff.close()
g.search('Passo Fundo')
#ff.close()
fim = time.time()#Mede tempo de execução
print(fim - inicio)#Mede tempo de execução