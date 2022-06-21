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
driver.get('https://5228089-sb1.app.netsuite.com/app/common/item/item.nl?itemtype=InvtPart&subtype=&isserialitem=F&islotitem=F')
# 点击登录
try:
    time.sleep(2)
    ele=driver.find_element_by_id("login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 货品创建流程
# ----------------------------------------------------一.货品创建---------------------------------------------------------
# 01.引用商品
commodity = driver.find_element_by_css_selector('#parent_actionbuttons_custitem_hq_sku_spu_v_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(commodity).click(commodity).perform()

commodity_list = driver.find_element_by_css_selector('#custitem_hq_sku_spu_v_popup_list')
webdriver.ActionChains(driver).move_to_element(commodity_list).click(commodity_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('SPU0000000015773')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

# 02.规格1[同一商品下不能有规格相同的货品]
Specifications01 = driver.find_element_by_css_selector('#parent_actionbuttons_custitem_hq_sku_spu_spec_1_value_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(Specifications01).click(Specifications01).perform()

specs01_list = driver.find_element_by_css_selector('#custitem_hq_sku_spu_spec_1_value_popup_list')
webdriver.ActionChains(driver).move_to_element(specs01_list).click(specs01_list).perform()

driver.find_element_by_css_selector('#st').send_keys('0.1 x 0.4mm')  # 0.1 x 0.3mm/0.1 x 0.4mm/0.1 x 0.5mm

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()
time.sleep(2)

# 03.规格2
Specifications02 = driver.find_element_by_css_selector('#parent_actionbuttons_custitem_hq_sku_spu_2_value_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(Specifications02).click(Specifications02).perform()

specs02_list = driver.find_element_by_css_selector('#custitem_hq_sku_spu_2_value_popup_list')
webdriver.ActionChains(driver).move_to_element(specs02_list).click(specs02_list).perform()

driver.find_element_by_css_selector('#st').send_keys('10mg/ml')  # 10mg/ml,11mg/ml,12mg/ml

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()
time.sleep(2)

# 04.保存
try:
    driver.find_element_by_css_selector('#btn_secondarymultibutton_submitter').click()
    time.sleep(5)
except Exception as e:
    print('货品创建失败了：{}'.format(e))

# 05.获取货品编码
product_code = driver.find_element_by_css_selector('#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div').get_attribute('textContent')
print('货品创建成功了！')
print('货品编码：{}'.format(product_code))

# 06.关闭浏览器
time.sleep(1)
driver.quit()

