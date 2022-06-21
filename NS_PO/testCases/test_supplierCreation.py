# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.supplierCreation_page import SupplierCreationPage
from NS_PO.pageObjects.login_page import LoginPage
from TestData import NsData as ld
import allure

sc = ld.supplierCreation_data

@allure.feature('创建供应商')
@pytest.mark.run(order=1)  # 标签
class TestSupplierCreation:

    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        option = webdriver.ChromeOptions()
        option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 打开浏览器,访问登录页面
        self.url = 'https://5228089-sb1.app.netsuite.com/app/common/entity/vendorlist.nl?whence='
        LoginPage().login_success(self.driver, self.url)
        self.PC = SupplierCreationPage(self.driver)

        yield self.driver
        self.driver.quit()

    # 正常场景:供应商创建成功
    @allure.title('供应商创建成功')
    @allure.severity("Minor")
    def test_supplier_success(self):
        # 01.点击-新建供应商
        self.PC.new_supplier()
        # 02.供应商详情
        self.PC.supplier_details(sc['brand'], sc['address'], sc['register'], sc['returns'], sc['currency'], sc['department'], sc['subject'])

if __name__ == '__main__':

    pytest.main(['test_supplierCreation.py', '-s'])  # -s  显示打印