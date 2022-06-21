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
driver.get('https://5228089-sb1.app.netsuite.com/app/accounting/transactions/transactionlist.nl?Transaction_TYPE=PurchOrd&whence=')
# 点击登录
try:
    ele=driver.find_element_by_id("login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 采购单副本流程
# ----------------------------------------------------01.搜索采购单---------------------------------------------------------
# 01.全局搜索
driver.find_element_by_css_selector('#NS_MENU_ID0-item1 > a').click()
time.sleep(2)

# 02.输入采购单号[PO000013480(VD000003071 LLJ-领用专用)]  [PO000013491(VD000002760 深圳市米茄科技有限公司)]
driver.find_element_by_css_selector('#Transaction_NUMBERTEXT').send_keys('PO000013491')

# 03.提交
driver.find_element_by_css_selector('#secondarysubmitter').click()
time.sleep(3)

# ----------------------------------------------------02.副本创建审核-------------------------------------------------------
# 04.查看
driver.find_element_by_css_selector('#row0 > td.listtextctr.uir-list-row-cell > a.dottedlink.viewitem').click()
time.sleep(2)

# 05.操作-制作副本
MakeCopy = driver.find_element_by_css_selector('#spn_ACTIONMENU_d1 > span.pgm_bg > a')
webdriver.ActionChains(driver).move_to_element(MakeCopy).perform()
driver.find_element_by_css_selector('#nl2 > a > span').click()

# 06.返回原default
driver.switch_to.default_content()
time.sleep(2)

# 07.保存
try:
    driver.find_element_by_css_selector('#btn_secondarymultibutton_submitter').click()
    time.sleep(3)
except Exception as e:
    print('采购单创建失败了：{}'.format(e))

# 8.获取采购单号
POID = driver.find_element_by_css_selector('#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div.uir-record-id').get_attribute('textContent')
print('采购单创建成功了！')
print('采购单号：{}'.format(POID))
time.sleep(2)

# 9.审批通过
driver.find_element_by_css_selector('#custpageworkflow398').click()

# 10.关闭浏览器
time.sleep(3)
driver.quit()
