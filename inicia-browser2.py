from selenium import webdriver

class Google:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'lst-ib'
        self.btn_search = 'btnK'

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)


ff = webdriver.Firefox()


g = Google(ff)

#g.navigate()

#envio = ff.find_element_by_id('lst-ib')

#envio.send_keys('python')