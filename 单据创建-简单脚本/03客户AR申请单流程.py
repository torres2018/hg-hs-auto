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
driver.get('https://5228089-sb1.app.netsuite.com/app/common/custom/custrecordentry.nl?rectype=195')
# 点击登录
try:
    ele=driver.find_element_by_css_selector("#login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 客户AR申请单流程
# ----------------------------------------------------01.客户AR申请单[增加额度]---------------------------------------------------------

# 01.客户名称
driver.find_element_by_css_selector('#custrecord_hg_cus_cusname_display').send_keys('CU000024813 HG-UI测试专用')
time.sleep(3)

# 02.申请类型【信用额度发货】
driver.find_element_by_css_selector('#inpt_custrecord_hg_cus_sqlx3_arrow').click()
time.sleep(2)
driver.find_element_by_css_selector('#nl4').click()
time.sleep(2)

# 03.申请金额
driver.find_element_by_css_selector('#custrecord_hg_cus_changecredit_formattedValue').send_keys(1000)
time.sleep(2)

# 04.到期时间
driver.find_element_by_css_selector('#custrecord_hg_cus_rq').send_keys('2025-02-16')
time.sleep(2)

# 05.备注说明【富文本】
driver.switch_to.frame('ext-gen57')#切换到目标frame
driver.find_element('id', 'ext-gen72').send_keys('hello')
driver.switch_to.default_content()#切换到默认内容
time.sleep(2)

# 06.保存[#btn_multibutton_submitter]
driver.find_element_by_css_selector('#btn_multibutton_submitter').click()
time.sleep(3)

# 07.提交审批
driver.find_element_by_css_selector('#custpageworkflow210').click()
time.sleep(3)

# 08.审批确认
driver.find_element_by_css_selector('#custpageworkflow217').click()
time.sleep(3)

# 09.再次审批确认
driver.find_element_by_css_selector('#custpageworkflow239').click()
time.sleep(2)

# 10.标记已冲减
try:
    driver.find_element_by_css_selector('#custpageworkflow2190').click()
    print('客户AR申请单创建成功!')
    time.sleep(3)
except Exception as e:
    print('客户AR申请单创建失败：{}'.format(e))

# --------------------------02.已冲减AR申请单[清空额度，审批完成才能重新申请AR---------------------------------------------------
# 1.事务处理
transaction = driver.find_element_by_xpath('//*[@id="ns-header-menu-main-item1"]/a/span')
webdriver.ActionChains(driver).move_to_element(transaction).perform()
time.sleep(3)

# 2.销售
sale = driver.find_element_by_xpath('//*[@class="ns-menu uir-menu-main ns-menubar"]/li[2]/ul/li[6]')
webdriver.ActionChains(driver).move_to_element(sale).perform()
time.sleep(3)

# 3.客户AR申请单
driver.find_element_by_xpath('//*[@class="ns-menu uir-menu-main ns-menubar"]/li[2]/ul/li[6]/ul/li[13]').click()
time.sleep(5)

# 4.查看
driver.find_element_by_css_selector('#row0 > td:nth-child(3) > a.dottedlink.viewitem').click()
time.sleep(3)

# 5.确认调整【确认生成一样的效果】
driver.find_element_by_css_selector('#custpageworkflow693').click()

#8.关闭浏览器
time.sleep(5)
driver.quit()

