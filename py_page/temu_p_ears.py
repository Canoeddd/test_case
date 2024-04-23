import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_locator.temu_locator import *
from page_locator.code_detail_locator import *
from py_page.base_p import BasePage
from page_locator.public import ears, by_method

class TemuEars():
    def __init__(self):
        self.ears_temu = BasePage(ears)
    # def click_store(self):
    #     self.find_and_click(By.XPATH, ele_temu)
    #     return self

# temu店铺页

    def first_des(self):

        ele = self.ears_temu.find(by_method, ele_coupon1)
        first_des = ele.text
        return first_des

    def sec_des(self):
        ele = self.ears_temu.find(by_method, ele_coupon2)
        sec_des = ele.text
        return sec_des

    def link_ele(self):
        link_element = self.ears_temu.find(by_method, ele_get_deal)
        get_deal_link = link_element.get_attribute('href')
        return get_deal_link

# code详情页

    def first_code(self):
        self.ears_temu.find_and_click(by_method,ele_codeA1)
        self.ears_temu.ad_close()

        # current_url = self.ears_temu.driver.current_url
        # print(current_url)
        # if "#google_vignette" in current_url:
        #     a = self.ears_temu.driver.switch_to.frame("aswift_6")
        #     close_button = self.ears_temu.find(by_method, "//div[@id='dismiss-button']")
        #     close_button.click()
        #     # actions = ActionChains(self.ears_temu.driver)
        #     # actions.move_to_element(close_button).click().perform()
        #     self.ears_temu.driver.switch_to.default_content()
        # else:
        #     pass

        # popup = self.ears_temu.find(By.ID, "popup")
        # if popups:
        #     # 执行关闭弹窗的操作
        #     close_button = popup.find_element(By.CLASS_NAME, "close-button")
        #     close_button.click()
        # except:
        #     # 弹窗没有出现，执行其他操作
        #     pass

        code_text = self.ears_temu.find(by_method, ele_code_text).text
        return code_text

    def copy_code(self):
        self.ears_temu.find_and_click(by_method, ele_copy)          # 点击copy code按钮进入弹窗
        print("*-*" * 28,"【点击copy_code进入弹窗】","*-*" * 28)

    def code_link(self):                                               # 获取code的link链接
        code_link = self.ears_temu.find(by_method, ele_code_link)
        print("*-*" * 28,"【获取code的link链接】","*-*" * 28)
        get_code_link = code_link.get_attribute('href')
        return get_code_link

    def sec_code(self):
        # self.ears_temu.back_p()
        # self.ears_temu.ad_close()
        # try:
        #     parent_element = self.ears_temu.find(by_method, '/html/body/ins[2]/div')
        #     shadow_root = self.ears_temu.driver.execute_script('return arguments[0].shadowRoot;', parent_element)
        #     desired_element = shadow_root.find_element(by_method, "//path[@stroke='#FAFAFA']")
        #     desired_element.click()
        #
        # except:
        #     pass


        element = self.ears_temu.find(by_method, ele_codeA2)

        self.ears_temu.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        # self.ears_temu.driver.execute_script('arguments[0].scrollIntoview();',element)

        self.ears_temu.ad_close()

        code_text = self.ears_temu.find(by_method, ele_code_text).text
        return code_text



