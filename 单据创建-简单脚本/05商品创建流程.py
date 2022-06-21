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
driver.get('https://5228089-sb1.app.netsuite.com/app/common/custom/custrecordentry.nl?rectype=263&whence=')
# 点击登录
try:
    ele=driver.find_element_by_id("login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 商品创建流程
# ----------------------------------------------------一.商品创建---------------------------------------------------------
# 01.商品名称
str1 = 'test'
str2 = str(int(time.time()))
pro_name = str1+str2
driver.find_element_by_css_selector('#altname').send_keys(pro_name)

# 02.采购名称
str3 = 'purchase'
str4 = str(int(time.time()))
pur_name = str3+str4
driver.find_element_by_css_selector('#custrecord_hq_spu_p_name').send_keys(pur_name)

# 03.品牌
brand = driver.find_element_by_css_selector('#parent_actionbuttons_custrecord_hq_spu_bland_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(brand).click(brand).perform()

brand_list = driver.find_element_by_css_selector('#custrecord_hq_spu_bland_popup_list')
webdriver.ActionChains(driver).move_to_element(brand_list).click(brand_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('Eleaf牌/依丽芙牌')

driver.find_element_by_css_selector('#Search').click()

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

# 04.规格1
specs01 = driver.find_element_by_css_selector('#parent_actionbuttons_custrecord_hg_spu_soec_1_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(specs01).click(specs01).perform()

specs01_list = driver.find_element_by_css_selector('#custrecord_hg_spu_soec_1_popup_list')
webdriver.ActionChains(driver).move_to_element(specs01_list).click(specs01_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('Type')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()
time.sleep(2)

# 05.规格2
specs02 = driver.find_element_by_css_selector('#parent_actionbuttons_custrecord_hg_spu_spec_2_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(specs02).click(specs02).perform()

specs02_list = driver.find_element_by_css_selector('#custrecord_hg_spu_spec_2_popup_list')
webdriver.ActionChains(driver).move_to_element(specs02_list).click(specs02_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('Strength')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()
time.sleep(2)

# 06.报关类型
declare_at_customs = driver.find_element_by_css_selector('#inpt_custrecord_hq_bglx2_arrow')
webdriver.ActionChains(driver).move_to_element(declare_at_customs).click(declare_at_customs).perform()

driver.find_element_by_css_selector('#nl3').click()

# 07.进销性质
Purchase_pin = driver.find_element_by_css_selector('#inpt_custrecord_hq_jxxx13_arrow')
webdriver.ActionChains(driver).move_to_element(Purchase_pin).click(Purchase_pin).perform()

driver.find_element_by_css_selector('#nl8').click()

# 08.交期
driver.find_element_by_css_selector('#custrecord_hq_jiaoqi').send_keys(30)

# 09.类别
category = driver.find_element_by_css_selector('#inpt_custrecord_hg_d_cd7_arrow')
webdriver.ActionChains(driver).move_to_element(category).click(category).perform()

driver.find_element_by_css_selector('#nl16').click()

# 10.是否为铺货
Distribution = driver.find_element_by_css_selector('#inpt_custrecord_hg_if_pu_df8_arrow')
webdriver.ActionChains(driver).move_to_element(Distribution).click(Distribution).perform()

driver.find_element_by_css_selector('#nl19').click()

# 11.主供应商
supplier = driver.find_element_by_css_selector('#parent_actionbuttons_custrecord_hg_mubd_vend_rf_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(supplier).click(supplier).perform()

supplier_list = driver.find_element_by_css_selector('#custrecord_hg_mubd_vend_rf_popup_list')
webdriver.ActionChains(driver).move_to_element(supplier_list).click(supplier_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('VD000002760 深圳市米茄科技有限公司')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

# 12.单位
unit = driver.find_element_by_css_selector('#parent_actionbuttons_custrecord_hg_spu_unit_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(unit).click(unit).perform()

unit_list = driver.find_element_by_css_selector('#custrecord_hg_spu_unit_popup_list')
webdriver.ActionChains(driver).move_to_element(unit_list).click(unit_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('个')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

# 13.库存分类·一级
classification01 = driver.find_element_by_css_selector('#inpt_custrecord_hg_sd_caigsw9_arrow')
webdriver.ActionChains(driver).move_to_element(classification01).click(classification01).perform()

driver.find_element_by_css_selector('#nl24').click()
time.sleep(2)

# 14.库存分类·二级
classification02 = driver.find_element_by_css_selector('#inpt_custrecord_hq_cgfl110_arrow')
webdriver.ActionChains(driver).move_to_element(classification02).click(classification02).perform()

driver.find_element_by_css_selector('#nl36').click()
time.sleep(2)

# 15.部门
department = driver.find_element_by_css_selector('#custrecord_hg_department_spu_popup_list')
webdriver.ActionChains(driver).move_to_element(department).click(department).perform()
time.sleep(1)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').click()

driver.find_element_by_css_selector('#update').click()
time.sleep(2)

# 16.保存
try:
    driver.find_element_by_css_selector('#btn_secondarymultibutton_submitter').click()
    time.sleep(3)
except Exception as e:
    print('商品创建失败了：{}'.format(e))

# 14.获取商品编码
Commodity_code = driver.find_element_by_css_selector('#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div').get_attribute('textContent')
print('商品创建成功了！')
print('商品编码：{}'.format(Commodity_code))

# 17.关闭浏览器
time.sleep(5)
driver.quit()
