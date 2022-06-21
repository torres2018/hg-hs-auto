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
driver.get('https://5228089-sb1.app.netsuite.com/app/common/item/itemlist.nl?whence=')
# 点击登录
try:
    ele=driver.find_element_by_id("login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 外部采购价创建流程
# --------------------------------------------一.查找外部采购价---------------------------------------------------------
# 01.全局搜索
driver.find_element_by_css_selector('#NS_MENU_ID0-item1 > a').click()
time.sleep(2)

# 02.输入货品编码
driver.find_element_by_css_selector('#Item_NAME').send_keys('PN0000000057827')

# 03.提交
driver.find_element_by_css_selector('#submitter').click()
time.sleep(3)

# 04.查看
driver.find_element_by_css_selector('#row0 > td.listtextctr.uir-list-row-cell > a.dottedlink.viewitem').click()
time.sleep(2)

# 05.外部采购价格
driver.find_element_by_css_selector('#custom31txt').click()
time.sleep(2)

# 06.新建【货品外部采购价格】
driver.find_element_by_css_selector('#newrecrecmachcustrecord_hg_price_item').click()
time.sleep(3)

# --------------------------------------------二.填写外部采购价格单---------------------------------------------------------
# 01.名称
str1 = 'LI'
str2 = str(int(time.time()))
pro_name = str1+str2
driver.find_element_by_css_selector('#name').send_keys(pro_name)

# 02.供应商
supplier = driver.find_element_by_css_selector('#parent_actionbuttons_custrecord_hg_pric_vend_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(supplier).click(supplier).perform()

supplier_list = driver.find_element_by_css_selector('#custrecord_hg_pric_vend_popup_list')
webdriver.ActionChains(driver).move_to_element(supplier_list).click(supplier_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('VD000002760 深圳市米茄科技有限公司')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

# 03.汇率记录
exchange_rate = driver.find_element_by_css_selector('#inpt_custrecord_hg_re_record1_arrow')
webdriver.ActionChains(driver).move_to_element(exchange_rate).click(exchange_rate).perform()

driver.find_element_by_css_selector('#nl5').click()
time.sleep(1)

# 04.报价币种采购价格
driver.find_element_by_css_selector('#custrecord_hq_gcjj1_formattedValue').send_keys(100)
time.sleep(1)

# 05.开票税点
Tax_point = driver.find_element_by_css_selector('#inpt_custrecord_hg_kp_pre2_arrow')
webdriver.ActionChains(driver).move_to_element(Tax_point).click(Tax_point).perform()

driver.find_element_by_css_selector('#nl12').click()
time.sleep(1)

# 06.未含税采购价格保留几位小数
point = driver.find_element_by_css_selector('#inpt_custrecord_hq_sku_price_dot3_arrow')
webdriver.ActionChains(driver).move_to_element(point).click(point).perform()

driver.find_element_by_css_selector('#nl28').click()
time.sleep(1)

# 07.最终采购价格保留小数位
pur_point = driver.find_element_by_css_selector('#inpt_custrecord_hg_biao_bao_date4_arrow')
webdriver.ActionChains(driver).move_to_element(pur_point).click(pur_point).perform()

driver.find_element_by_css_selector('#nl32').click()
time.sleep(1)

# 08.是否默认
default = driver.find_element_by_css_selector('#inpt_custrecord_hg_if_defautkes5_arrow')
webdriver.ActionChains(driver).move_to_element(default).click(default).perform()

driver.find_element_by_css_selector('#nl35').click()
time.sleep(1)

# 09.保存
try:
    driver.find_element_by_css_selector('#btn_secondarymultibutton_submitter').click()
    time.sleep(3)
    print('外部采购价格创建成功！')
except Exception as e:
    print("外部采购价格创建失败：{}".format(e))

# 10.弹出框确认
alertObject = driver.switch_to.alert
alertObject.accept()
time.sleep(3)

# ----------------------------------------三.审批货品外部采购价格-------------------------------------------------------
# 01.外部采购价格
driver.find_element_by_css_selector('#custom31txt').click()
time.sleep(2)

# 02.选择需要审核的外部采购价[将元素内itemrow0改成itemrow1，则选择下一个]
driver.find_element_by_css_selector('#recmachcustrecord_hg_price_itemrow0 > td:nth-child(2) > a').click()
time.sleep(2)

# 03.审批通过
try:
    driver.find_element_by_css_selector('#custpageworkflow344').click()
    time.sleep(2)
except Exception as e:
    print('外部采购价格审批失败：{}'.format(e))

# 04.获取外部采购单号
pur_code = driver.find_element_by_css_selector('#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div').get_attribute('textContent')
print('外部采购价格审批通过！')
print('外部采购价格单号：{}'.format(pur_code))

# 05.关闭浏览器
time.sleep(3)
driver.quit()
