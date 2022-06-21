# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.purchasePrice_page import PurchasePricePage
from NS_PO.pageObjects.login_page import LoginPage
from TestData import NsData as ld
import allure

pp_data = ld.purchasePrice_data

@allure.feature('创建外部采购价')
@pytest.mark.run(order=8)  # 标签
class TestPurchasePrice:

    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        # 打开浏览器,访问登录页面
        option = webdriver.ChromeOptions()
        option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = 'https://5228089-sb1.app.netsuite.com/app/common/item/itemlist.nl?whence='
        LoginPage().login_success(self.driver, self.url)
        self.PC = PurchasePricePage(self.driver)

        yield self.driver
        self.driver.quit()

    # 正常场景:外部采购价创建成功
    @allure.title('外部采购价创建成功')
    @allure.severity("Minor")
    def test_price_success(self):
        # 01.查找货品外部采购价
        self.PC.global_search()
        # 02.填写外部采购价格单
        self.PC.fill_in_documents(pp_data['supplier'], pp_data['price'])
        # 03.审批货品外部采购价格
        self.PC.approval_document()

if __name__ == '__main__':

    pytest.main(['test_purchasePrice.py', '-s'])  # -s  显示打印
