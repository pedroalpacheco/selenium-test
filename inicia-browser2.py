from selenium import webdriver


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
#g.search('Pedro Alexandr Pacheco')
g.lucky('Pedro Alexandr Pacheco')

#g.navigate()

#envio = ff.find_element_by_id('lst-ib')

#envio.send_keys('python')