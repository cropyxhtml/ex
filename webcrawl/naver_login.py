from selenium import webdriver
from bs4 import BeautifulSoup


class NaverLogin:
    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path='C:/Users/ezen/PycharmProjects/tensorflow190803/webcrawl/data/chromedriver')
        self.driver.implicitly_wait(3)
        self.driver.get(url)

    def auto_login(self):
        self.driver.find_element_by_name('id').send_keys('identity')
        self.driver.find_element_by_name('pw').send_keys('pswd')
        self.driver.implicitly_wait(3)

        self.find_elemnt_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(3)

        driver.get('https://order.pay.naver.com/home')
        html = self.driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        notices = soup.select('div.p_inr > div.p_info > a > span')

        for i in notices:
            print(i.text.strip())