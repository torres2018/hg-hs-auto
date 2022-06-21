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
driver.get('https://5228089-sb1.app.netsuite.com/app/common/entity/vendorlist.nl?whence=')
# 点击登录
try:
    ele=driver.find_element_by_id("login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 创建供应商流程
# ----------------------------------------------------01.创建供应商---------------------------------------------------------
# 01.点击【新建供应商】
driver.find_element_by_css_selector('#new').click()
time.sleep(2)

# ----------------------------------------------------02.供应商详情---------------------------------------------------------
# 01.公司名称
dateNow = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
name = 'LLJ专用'+dateNow
driver.find_element_by_css_selector('#companyname').send_keys(name)
time.sleep(2)

# 02.供应商类别
SupplierCategory = driver.find_element_by_css_selector('#inpt_custentity_hg_vend_type2_arrow')
webdriver.ActionChains(driver).move_to_element(SupplierCategory).click(SupplierCategory).perform()
driver.find_element_by_css_selector('#nl6').click()
time.sleep(2)

# 03.品牌
brand = driver.find_element_by_css_selector('#parent_actionbuttons_custentity_hq_pinpai1_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(brand).click(brand).perform()

brand_list = driver.find_element_by_css_selector('#custentity_hq_pinpai1_popup_list')
webdriver.ActionChains(driver).move_to_element(brand_list).click(brand_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('Eleaf牌/依丽芙牌')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

# 04.中文地址
driver.find_element_by_css_selector('#custentity_hg_china_address').send_keys('上海普陀区长风公园')
time.sleep(2)

# 05.注册国家
country = driver.find_element_by_css_selector('#parent_actionbuttons_custentity_hg_zhuc_c_country_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(country).click(country).perform()

country_list = driver.find_element_by_css_selector('#custentity_hg_zhuc_c_country_popup_list')
webdriver.ActionChains(driver).move_to_element(country_list).click(country_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('China')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

# 06.供货模式
SupplyMode = driver.find_element_by_css_selector('#inpt_custentity_hg_vendor_deli_mode3_arrow')
webdriver.ActionChains(driver).move_to_element(SupplyMode).click(SupplyMode).perform()
driver.find_element_by_css_selector('#nl10').click()
time.sleep(2)

# 07.货物来源
SourceOfGoods = driver.find_element_by_css_selector('#inpt_custentity14_arrow')
webdriver.ActionChains(driver).move_to_element(SourceOfGoods).click(SourceOfGoods).perform()
driver.find_element_by_css_selector('#nl15').click()
time.sleep(2)

# 08.退货地址
driver.find_element_by_css_selector('#custentity_hg_caigou_tuihuo').send_keys('英国伦敦')
time.sleep(1)

# 09.结算方式
SettlementMethod = driver.find_element_by_css_selector('#inpt_terms6_arrow')
webdriver.ActionChains(driver).move_to_element(SettlementMethod).click(SettlementMethod).perform()
driver.find_element_by_css_selector('#nl19').click()
time.sleep(2)

# 10.货币
currency = driver.find_element_by_css_selector('#custentity_hg_c_dsss_fs > span.uir-field-widget')
webdriver.ActionChains(driver).move_to_element(currency).click(currency).perform()
time.sleep(3)
driver.find_element_by_css_selector('#st').send_keys('CNY')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

driver.find_element_by_css_selector('#update').click()

# 11.部门
department = driver.find_element_by_css_selector('#custentity_hg_department_vend_popup_list')
webdriver.ActionChains(driver).move_to_element(department).click(department).perform()
time.sleep(3)
driver.find_element_by_css_selector('#st').send_keys('B2B事业部')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').click()

driver.find_element_by_css_selector('#update').click()

# 12.收件人
driver.find_element_by_css_selector('#custentity_vendor_receiver').send_keys('李连军')

# 12.城市
driver.find_element_by_css_selector('#custentity_vendor_city').send_keys('上海')

# 12.地址
driver.find_element_by_css_selector('#custentity_vendor_location').send_keys('南翔')

# 12.州、省
driver.find_element_by_css_selector('#custentity_vendor_province').send_keys('祥和雅苑')

# 12.邮编
driver.find_element_by_css_selector('#custentity_vendor_zipcode').send_keys('66666666')

# 12.电话
driver.find_element_by_css_selector('#custentity_vendor_phone_number').send_keys('15601608610')

# 13.收件国家
RecipientCountry = driver.find_element_by_css_selector('#parent_actionbuttons_custentity_vendor_country_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(RecipientCountry).click(RecipientCountry).perform()

Recipient_country_list = driver.find_element_by_css_selector('#custentity_vendor_country_popup_list')
webdriver.ActionChains(driver).move_to_element(Recipient_country_list).click(Recipient_country_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('中国')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').click()

# 14.统一计量单位
measurement = driver.find_element_by_css_selector('#parent_actionbuttons_custentity_hg_sol_unite_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(measurement).click(measurement).perform()

measurement_list = driver.find_element_by_css_selector('#custentity_hg_sol_unite_popup_list')
webdriver.ActionChains(driver).move_to_element(measurement_list).click(measurement_list).perform()
time.sleep(3)

driver.find_element_by_css_selector('#st').send_keys('个')

driver.find_element_by_css_selector('#Search').click()
time.sleep(2)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').click()

# 15.采购主体
ProcurementSubject = driver.find_element_by_css_selector('#parent_actionbuttons_subsidiary_fs > a:nth-child(2)')
webdriver.ActionChains(driver).move_to_element(ProcurementSubject).click(ProcurementSubject).perform()

ProcurementSubject_list = driver.find_element_by_css_selector('#subsidiary_popup_list')
webdriver.ActionChains(driver).move_to_element(ProcurementSubject_list).click(ProcurementSubject_list).perform()
time.sleep(5)

driver.find_element_by_css_selector('#st').send_keys('爱奇迹（深圳）技术有限公司')

driver.find_element_by_css_selector('#Search').click()
time.sleep(3)

driver.find_element_by_css_selector('#inner_popup_div > table > tbody > tr > td:nth-child(2) > a').click()

# 16.返回原default
driver.switch_to.default_content()
time.sleep(2)

# 17.保存
try:
    driver.find_element_by_css_selector('#btn_secondarymultibutton_submitter').click()
    time.sleep(2)
except Exception as e:
    print('供应商创建失败了：{}'.format(e))

# ----------------------------------------------------03.供应商编号---------------------------------------------------------
# 18.获取供应商编码
supplier_code = driver.find_element_by_css_selector('#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div').get_attribute('textContent')
print('供应商创建成功了！')
print('供应商编号：{}'.format(supplier_code))

# 19.关闭浏览器
time.sleep(3)
driver.quit()
