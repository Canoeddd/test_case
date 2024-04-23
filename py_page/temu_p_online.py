
from selenium.webdriver.common.by import By

from page_locator.temu_locator import  *
from page_locator.code_detail_locator import *
from py_page.base_p import BasePage
from page_locator.public import online, by_method

class TemuOnline():
    def __init__(self):
        self.online_temu = BasePage(online)
    # def click_store(self):
    #     self.find_and_click(By.XPATH, ele_temu)
    #     return self



# temu店铺页

    def first_des(self):

        ele = self.online_temu.find(by_method, ele_coupon1)
        first_des = ele.text
        return first_des                # 返回第一张coupon的des

    def sec_des(self):
        ele = self.online_temu.find(by_method, ele_coupon2)
        sec_des = ele.text
        return sec_des                  # 返回第二张coupon的des

    def link_ele(self):
        link_element = self.online_temu.find(by_method, ele_get_deal)
        get_deal_link = link_element.get_attribute('href')
        return get_deal_link            # 返回get deal的affi_link


 # code详情页

    def first_code(self):
        element = self.online_temu.find(by_method, ele_codeB1)
        self.online_temu.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.online_temu.ad_close()
        code_text = self.online_temu.find(by_method, ele_code_online).text
        return code_text               # 返回第一张coupon的code码

    def copy_code(self):
        a = self.online_temu.find_and_click(by_method, ele_copy_code)         # 点击copy code按钮进入弹窗
        print("*-*" * 28,"【点击copy_code进入弹窗】","*-*" * 28)

    def code_link(self):                                                      # 获取code的link链接
        code_link = self.online_temu.find(by_method, ele_code_link)

        print("*-*" * 28,"【获取code的link链接】","*-*" * 28)
        get_code_link = code_link.get_attribute('href')
        return get_code_link

    def sec_code(self):
        # self.online_temu.back_p()
        # self.online_temu.ad_close()
        element = self.online_temu.find(by_method, ele_codeB2)
        self.online_temu.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        print("*-*" * 28,"【点击第二张coupon】","*-*" * 28)
        self.online_temu.ad_close()
        print("*-*" * 28,"【进入第二张coupon详情页】","*-*" * 28)
        code_text = self.online_temu.find(by_method, ele_code_online).text
        return code_text              # 返回第二张coupon的code码