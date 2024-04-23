
from selenium.webdriver.common.by import By

from page_locator.temu_locator import  *
from page_locator.code_detail_locator import *
from py_page.base_p import BasePage
from page_locator.public import found, by_method

class TemuFound():
    def __init__(self):
        self.found_temu = BasePage(found)
    # def click_store(self):
    #     self.find_and_click(By.XPATH, ele_temu)
    #     return self

# temu店铺页

    def first_des(self):

        ele = self.found_temu.find(by_method, ele_coupon1)
        first_des = ele.text
        return first_des

    def sec_des(self):
        ele = self.found_temu.find(by_method, ele_coupon2)
        sec_des = ele.text
        return sec_des

    def link_ele(self):
        link_element = self.found_temu.find(by_method, ele_get_deal)
        get_deal_link = link_element.get_attribute('href')
        return get_deal_link

# code详情页

    def first_code(self):
        element = self.found_temu.find(by_method,ele_codeB1)
        self.found_temu.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.found_temu.ad_close()
        code_text = self.found_temu.find(by_method, ele_code_online).text
        return code_text

    def copy_code(self):
        a = self.found_temu.find_and_click(by_method, ele_copy_code)   # 点击copy code按钮进入弹窗
        print("*-*" * 28,"【点击copy_code进入弹窗】","*-*" * 28)

    def code_link(self):                                               # 获取code的link链接
        code_link = self.found_temu.find(by_method, ele_code_link)
        print("*-*" * 28,"【获取code的link链接】","*-*" * 28)
        get_code_link = code_link.get_attribute('href')
        return get_code_link

    def sec_code(self):
        # self.found_temu.back_p()
        # self.found_temu.ad_close()
        element = self.found_temu.find(by_method, ele_codeB2)

        self.found_temu.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.found_temu.ad_close()


        code_text = self.found_temu.find(by_method, ele_code_online).text
        return code_text



