# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.inventoryAdjustment_page import InventoryAdjustmentPage
from NS_PO.pageObjects.login_page import LoginPage
from TestData import NsData as ld
import allure

ia_data = ld.inventoryAdjustment_data

@allure.feature('库存调整单')
@pytest.mark.run(order=9)  # 标签
class TestInventoryAdjustment:

    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        # 打开浏览器,访问登录页面
        option = webdriver.ChromeOptions()
        option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = 'https://5228089-sb1.app.netsuite.com/app/accounting/transactions/invadjst.nl?whence='
        LoginPage().login_success(self.driver, self.url)
        self.PC = InventoryAdjustmentPage(self.driver)

        yield self.driver
        self.driver.quit()

    # 正常场景:库存调整单创建
    @allure.title('库存调整成功')
    @allure.severity("Minor")
    def test_stock_success(self):
        # 增加库存
        self.PC.inventory_adjustment(ia_data['company'],ia_data['product'],ia_data['warehouse'],ia_data['quantity'])

if __name__ == '__main__':

    pytest.main(['test_inventoryAdjustment.py', '-s'])  # -s  显示打印
