# /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time

"""
        绕过复杂的登录操作，比如图片验证码之类的，直接利用浏览器的数据，跟自己打开浏览器后，登录一些已登录的网站一样。
        from selenium import webdriver
        option = webdriver.ChromeOptions()
        option.add_argument(r'user-data-dir=C:\\Users\\username\AppData\Local\Google\Chrome\\User Data1')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        driver = webdriver.Chrome(options=option)
        driver.get('https://XXXXXXXXXXXXXXXXX/')
        使用环境：Win10系统，Chrome浏览器，webdriver要注意匹配自己当前的Chrome浏览器
        然后按照所示路径找到自己的User Data，把这个路径按照如图所示的代码加入参数里，
        最后，就可以随意打开已经有自动登录或者保存登录状态的网页了
        注意：User Data这个文件夹可以复制一份来给代码使用，一个User Data只能供一份代码使用，
        如果有webdriver在占用这个User Data(即有已在运行的Chrome浏览器进程,就会失败)
"""

# ------------------------------------------------------登录-------------------------------------------------------------
Option = webdriver.ChromeOptions()
Option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
Option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
driver = webdriver.Chrome(options=Option)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('https://5228089-sb1.app.netsuite.com/app/site/hosting/scriptlet.nl?script=161&deploy=1&compid=5228089_SB1&whence=')
# 点击登录
try:
    ele=driver.find_element_by_id("login-submit")
    ele.click()
    print('登录成功')
except:
    print('登录已存在！')
    pass
time.sleep(5)

# 采购单创建流程
# ----------------------------------------------------01.库存列表---------------------------------------------------------
# 4.输入货品编码
driver.find_element_by_xpath('//*[@id="itemid"]').send_keys('PN0000000057161')
time.sleep(3)

# 5.点击搜索
driver.find_element_by_xpath('//*[@id="search"]').click()
time.sleep(3)

# 6.添加进入购物车
driver.find_element_by_xpath('//*[@id="info_listrow0"]/td[2]/a').click()
time.sleep(5)

# ----------------------------------------------------02.选择PO类型-------------------------------------------------------
# 1.跳转到新窗口
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(5)

# 2.点击下拉
goshopping = driver.find_element_by_xpath('//*[@id="inpt_po_or_to1_arrow"]')
webdriver.ActionChains(driver).move_to_element(goshopping).click(goshopping).perform()

# 3.选择PO类型
po = driver.find_element_by_xpath('//*[@id="nl2"]').click()
time.sleep(5)

# ----------------------------------------------------03.购物车详情-------------------------------------------------------
# 进入添加购物车界面
# 01.选择仓库[//*[@class="uir-tooltip align_bottom_left uir-field-tooltip-wrapper"]/div/div/div[5]]
storehouse = driver.find_element_by_xpath('//*[@id="inpt_location3"]')
webdriver.ActionChains(driver).move_to_element(storehouse).click(storehouse).perform()
driver.find_element_by_xpath('//*[@id="nl51"]').click()

# 02.采购数量
driver.find_element_by_xpath('//*[@id="quantity_formattedValue"]').send_keys(1000)

# 03.结算方式
SettlementMethod = driver.find_element_by_xpath('//*[@id="inpt_settlement_method5"]')
webdriver.ActionChains(driver).move_to_element(SettlementMethod).click(SettlementMethod).perform()
driver.find_element_by_xpath('//*[@id="nl74"]').click()

# 04.供货模式[//*[@class="uir-tooltip align_top_right uir-field-tooltip-wrapper"]/div/div/div[4]]
deliveryOfGoods = driver.find_element_by_xpath('//*[@id="inpt_supply_mode6"]')
webdriver.ActionChains(driver).move_to_element(deliveryOfGoods).click(deliveryOfGoods).perform()
driver.find_element_by_xpath('//*[@id="nl91"]').click()

# 05.添加至PO购物车
driver.find_element_by_xpath('//*[@id="submitter"]').click()
time.sleep(5)

# 06.弹框确认
"""
首先，不是所有的alert都能叫做alert框。
JavaScript中，关于消息提示框的方法有三个（虽然都跟alert差不多）：
    01.alert(message)方法用于显示带有一条指定消息和一个 OK 按钮的警告框。
    02.confirm(message)方法用于显示一个带有指定消息和 OK 及取消按钮的对话框。如果用户点击确定按钮，则 confirm() 返回 true。
                    如果点击取消按钮，则 confirm() 返回 false。
    03.prompt(text,defaultText)方法用于显示可提示用户进行输入的对话框。如果用户单击提示框的取消按钮，则返回 null。如果用
                    户单击确认按钮，则返回输入字段当前显示的文本。

1.driver.switch_to.alert方法将webdriver作用域切换到alert提示框上, 
2.accept()点击确认按钮、dismiss()点击取消或者叉掉提示框.
"""
alertObject = driver.switch_to.alert
alertObject.accept()
time.sleep(5)

# 07.点击进入购物车列表
driver.find_element_by_xpath('//*[@id="ext-gen5"]/div/div/button[1]').click()
time.sleep(5)

# ----------------------------------------------------04.PO购物车列表-------------------------------------------------------
# 批量生成PO单
# 1.输入货品编码
driver.find_element_by_css_selector('#sub_itemid').send_keys('PN0000000057161')
time.sleep(2)

# 2.点击搜索
driver.find_element_by_xpath('//*[@id="search"]').click()
time.sleep(2)

# 3.勾选单据
driver.find_element_by_xpath('//*[@id="checkbox1_fs"]/img').click()
time.sleep(2)

"""
#4.清空并重新输入货品数量
driver.find_element_by_xpath('//*[@id="quantity1_formattedValue"]').clear()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="quantity1_formattedValue"]').send_keys(1000)
time.sleep(2)
"""

# 5.生成PO单
driver.find_element_by_xpath('//*[@id="submitter"]').click()
time.sleep(10)

# 6.点击刷新
for i in range(1,4):
    driver.find_element_by_xpath('//*[@id="refresh"]').click()
    time.sleep(3)

# 7.点击采购单链接，进入采购单
POID = driver.find_element_by_xpath('//*[@id="poidlink"]').get_attribute('textContent')
print('采购单号：{}'.format(POID))
time.sleep(2)
driver.find_element_by_xpath('//*[@id="poidlink"]').click()

# ----------------------------------------------------05.PO单审核-------------------------------------------------------
# 8.审批通过
driver.find_element_by_css_selector('#custpageworkflow398').click()

# 9.关闭浏览器
time.sleep(5)
driver.quit()
