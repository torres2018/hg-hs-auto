# /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time

# ------------------------------------------------------登录-------------------------------------------------------------
Option = webdriver.ChromeOptions()
Option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
Option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
driver = webdriver.Chrome(options=Option)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('https://5228089-sb1.app.netsuite.com/app/accounting/transactions/invadjst.nl?whence=')
# 点击登录
try:
    ele=driver.find_element_by_css_selector("#login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 库存调整单流程
# ----------------------------------------------------01.库存调整---------------------------------------------------------
# 1.附属公司
# a.下拉
company = driver.find_element_by_css_selector('#parent_actionbuttons_subsidiary_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(company).click(company).perform()
# b.列表
_list = driver.find_element_by_css_selector('#subsidiary_popup_list')
webdriver.ActionChains(driver).move_to_element(_list).click(_list).perform()
# c.输入子公司
driver.find_element_by_css_selector('#st').send_keys('母公司 : Felicita Vita Privat Ltd. : Geek Miracle International Holdings Limited : Geek Miracle (BVI) Limited : IMiracle (HK) Limited')
# d.点击搜索
driver.find_element_by_css_selector('#Search').click()
time.sleep(3)
# e.选择子公司
driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').click()
time.sleep(3)

# 2.调整科目
# a.下拉
course = driver.find_element_by_css_selector('#parent_actionbuttons_account_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(course).click(course).perform()
# b.列表
course_list = driver.find_element_by_css_selector('#account_popup_list')
webdriver.ActionChains(driver).move_to_element(course_list).click(course_list).perform()
# c.选择【#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a】
driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').click()
time.sleep(5)

# 3.货品【PN0000000057161】
# a.下拉
product = driver.find_element_by_css_selector('#parent_actionbuttons_inventory_item_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(product).click(product).perform()
# b.列表
_list = driver.find_element_by_css_selector('#item_popup_list')
webdriver.ActionChains(driver).move_to_element(_list).click(_list).perform()
time.sleep(6)
# c.输入【PN0000000057161】
driver.find_element_by_css_selector('#st').send_keys('PN0000000056956')
# d.点击搜索
driver.find_element_by_css_selector('#Search').click()
time.sleep(3)
# e.选择货品
driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr:nth-child(2) > td:nth-child(2) > a').click()
time.sleep(3)

# 4.地点[深圳仓-新香港公司]
driver.find_element_by_css_selector('#inventory_splits > tbody > tr.uir-machine-row.uir-machine-row-odd.listtextnonedit.uir-machine-row-focused > td:nth-child(3) > div').click()
# a.下拉
local = driver.find_element_by_css_selector('#parent_actionbuttons_inventory_location_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(local).click(local).perform()
# b.列表
local_list = driver.find_element_by_css_selector('#location_popup_list')
webdriver.ActionChains(driver).move_to_element(local_list).click(local_list).perform()
time.sleep(3)
# c.输入【深圳仓-新香港公司】
driver.find_element_by_css_selector('#st').send_keys('深圳仓-新香港公司')
# d.搜索
driver.find_element_by_css_selector('#Search').click()
time.sleep(2)
# e.选择该仓库
driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()
time.sleep(2)

# 5.调整数量
driver.find_element_by_css_selector('#inventory_splits > tbody > tr.uir-machine-row.uir-machine-row-odd.listtextnonedit.uir-machine-row-focused > td:nth-child(7) > div').click()
driver.find_element_by_css_selector('#adjustqtyby_formattedValue').send_keys(5000)
time.sleep(2)

# 6.添加
driver.find_element_by_css_selector('#inventory_addedit').click()
time.sleep(2)

# 7.保存
try:
    driver.find_element_by_css_selector('#secondarysubmitter').click()
    time.sleep(2)
except Exception as e:
    print('库存添加失败了:{}'.format(e))

# 8.库存调整单号
KCID = driver.find_element_by_css_selector('#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div').get_attribute('textContent')
print('PN0000000057161库存添加成功了')
print('库存调整单号：{}'.format(KCID))

#9.关闭浏览器
time.sleep(5)
driver.quit()
