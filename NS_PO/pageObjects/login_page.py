#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/5/31 9:55
# @Author  : Torres
# @Email   : 862578103@qq.com
# @File    : login_page.py
# @Software: PyCharm
from selenium import webdriver
import time

class LoginPage():
    def login_success(self,driver,nsurl):
        # 打开浏览器,访问登录页面
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = nsurl
        self.driver.get(self.url)
        # 点击登录
        try:
            time.sleep(2)
            ele = self.driver.find_element_by_id("login-submit")
            ele.click()
            print('登录成功')
        except:
            print('登录已存在！')
            pass

if __name__ == '__main__':
    Option = webdriver.ChromeOptions()
    Option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
    Option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
    driver = webdriver.Chrome(options=Option)
    nsurl = f"https://5228089-sb1.app.netsuite.com/app/common/custom/custrecordentry.nl?rectype=195"
    LoginPage().login_success(driver, nsurl)