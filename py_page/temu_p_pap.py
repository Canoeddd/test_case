
from selenium.webdriver.common.by import By

from page_locator.temu_locator import  *
from page_locator.code_detail_locator import *
from py_page.base_p import BasePage
from page_locator.public import pap, by_method

class TemuPap():
    def __init__(self):
        self.pap_temu = BasePage(pap)
    # def click_store(self):
    #     self.find_and_click(By.XPATH, ele_temu)
    #     return self

# temu店铺页

    def first_des(self):

        ele = self.pap_temu.find(by_method, ele_coupon1)
        first_des = ele.text
        return first_des

    def sec_des(self):
        ele = self.pap_temu.find(by_method, ele_coupon2)
        sec_des = ele.text
        return sec_des

    def link_ele(self):
        link_element = self.pap_temu.find(by_method, ele_get_deal)
        get_deal_link = link_element.get_attribute('href')
        return get_deal_link

# code详情页

    def first_code(self):
        self.pap_temu.find_and_click(by_method, ele_codeA1)
        self.pap_temu.ad_close()
        code_text = self.pap_temu.find(by_method, ele_code_text).text
        return code_text

    def copy_code(self):
        a = self.pap_temu.find_and_click(by_method, ele_copy)   # 点击copy code按钮进入弹窗
        print("*-*" * 28,"【点击copy_code进入弹窗】","*-*" * 28)

    def code_link(self):                                               # 获取code的link链接
        code_link = self.pap_temu.find(by_method, ele_code_link)
        print("*-*" * 28,"【获取code的link链接】", "*-*" * 28)
        get_code_link = code_link.get_attribute('href')
        return get_code_link

    def sec_code(self):
        # self.pap_temu.back_p()
        # self.pap_temu.ad_close()
        element = self.pap_temu.find(by_method, ele_codeA2)
        self.pap_temu.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.pap_temu.ad_close()
        code_text = self.pap_temu.find(by_method, ele_code_text).text
        return code_text