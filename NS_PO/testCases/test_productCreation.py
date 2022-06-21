# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.productCreation_page import ProductCreationPage
from NS_PO.pageObjects.login_page import LoginPage
from TestData import NsData as ld
import allure

pc_data = ld.productCreation_data

@allure.feature('创建商品')
@pytest.mark.run(order=6)  # 标签
class TestProductCreation:

    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        # 打开浏览器,访问登录页面
        option = webdriver.ChromeOptions()
        option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = 'https://5228089-sb1.app.netsuite.com/app/common/custom/custrecordentry.nl?rectype=263&whence='
        LoginPage().login_success(self.driver, self.url)
        self.PC = ProductCreationPage(self.driver)

        yield self.driver
        self.driver.quit()

    # 正常场景:商品创建成功
    @allure.title('商品创建成功')
    @allure.severity("Minor")
    def test_product_creation_success(self):
        self.PC.product_creation(pc_data['brand'],pc_data['norms'],pc_data['specs'],pc_data['date'],pc_data['supplier'],pc_data['unit'])


if __name__ == '__main__':

    pytest.main(['test_productCreation.py', '-s'])  # -s  显示打印
