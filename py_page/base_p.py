import time
import selenium

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from page_locator.public import ofs
from page_locator.public import by_method
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, url=ofs, driver=None):
        self.url = url
        if driver == None:

            chrome_options = Options()
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 只记录错误和警告
            s = Service(executable_path='chromedriver.exe')
            self.driver = webdriver.Chrome(service=s, options=chrome_options)
            self.driver.maximize_window()
            self.driver.get(url=self.url)
            self.driver.implicitly_wait(30)
            time.sleep(1)
        else:
            self.driver = driver



    def find(self, by, locator):
        ele_find = self.driver.find_element(by, locator)# 定位单个元素
        return ele_find


    def finds(self, by, locator):
        ele_finds = self.driver.find_elements(by, locator)      # 定位多个元素
        return ele_finds


    def find_and_click(self, by, locator):
        self.find(by, locator).click()                    # 点击


    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)         # 输入文字

    def back_p(self):
        self.driver.back()                          # 返回上一页




    def ad_close(self):                          # 关闭广告
        current_url = self.driver.current_url
        print(current_url)
        if "#google_vignette" in current_url:
            time.sleep(1)
            try:
                # iframes = self.finds(By.TAG_NAME, "iframe")
                iframe = self.find(By.XPATH, "/html/ins/div/iframe")
                self.driver.switch_to.frame(iframe)

                try:

                    # self.find(by_method, '//div[@aria-label="Close ad"]').click()
                    self.find(by_method, '//div[@id="dismiss-button"]').click()
                    time.sleep(1)

                    print("*-*" * 28,"【点击了有 X 的广告】","*-*" * 28)


                except :
                    print("*-*" * 28,"【出现没有 X 的广告】","*-*" * 28)
                    # self.driver.switch_to.default_content()
                    # iframe1 = self.find(by_method, "/html/ins/div/iframe")
                    # self.driver.switch_to.frame(iframe1)
                    iframe1 = self.find(by_method, "//iframe[@title='Advertisement']")
                    self.driver.switch_to.frame(iframe1)
                    # self.find(by_method, '//div[@aria-label="Close ad"]').click()
                    self.find(by_method, '//div[@id="dismiss-button"]').click()
                    time.sleep(1)

                    print("*-*" * 28,"【点击了没有 X 的广告】","*-*" * 28)

            except Exception as e:
                a = self.driver.page_source
                with open("a.html", mode="w", encoding="utf-8") as f:
                    f.write(a)
                raise e

            time.sleep(1)

            self.driver.switch_to.default_content()
            time.sleep(3)
        else:
            pass



