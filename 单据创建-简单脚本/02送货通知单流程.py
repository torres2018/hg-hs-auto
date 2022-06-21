# /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from datetime import date

# ------------------------------------------------------登录-------------------------------------------------------------
Option = webdriver.ChromeOptions()
Option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
Option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
driver = webdriver.Chrome(options=Option)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('https://5228089-sb1.app.netsuite.com/app/site/hosting/scriptlet.nl?script=226&deploy=1&compid=5228089_SB1&whence=')
# 点击登录
try:
    ele=driver.find_element_by_id("login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 送货通知单流程
# ----------------------------------------------------01.送货通知---------------------------------------------------------
#1.输入货品编码
driver.find_element_by_css_selector('#search_item_code').send_keys('PN0000000057161')
time.sleep(2)

#2.搜索
driver.find_element_by_css_selector('#search').click()
time.sleep(5)

#3.输入今天日期
tday = date.today()
driver.find_element_by_css_selector('#send_time').send_keys(str(tday))
time.sleep(2)

#4.输入发货数量
ele = driver.find_element_by_css_selector('#custpage_sendquantity1_formattedValue')
ele.clear()
time.sleep(2)
ele.send_keys(500)
time.sleep(2)

#5.点击提交
driver.find_element_by_css_selector('#submitter').click()
time.sleep(10)

#6.点击刷新
for i in range(1,4):
    driver.find_element_by_css_selector('#custpage_refresh').click()
    time.sleep(3)

#7.打印HS交货单号get_attribute('textContent')
JID = driver.find_element_by_css_selector('#info_listrow0 > td:nth-child(6)').get_attribute('textContent')
print('送货通知单号：{}'.format(JID))

#8.关闭浏览器
time.sleep(5)
driver.quit()


