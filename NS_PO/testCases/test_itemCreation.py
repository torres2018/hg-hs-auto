# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.itemCreation_page import ItemCreationPage
from NS_PO.pageObjects.login_page import LoginPage
from TestData import NsData as ld
import allure

ic_data = ld.itemCreation_data

@allure.feature('创建货品')
@pytest.mark.run(order=7)  # 标签
class TestItemCreation:

    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        # 打开浏览器,访问登录页面
        option = webdriver.ChromeOptions()
        option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = 'https://5228089-sb1.app.netsuite.com/app/common/item/item.nl?itemtype=InvtPart&subtype=&isserialitem=F&islotitem=F'
        LoginPage().login_success(self.driver, self.url)
        self.PC = ItemCreationPage(self.driver)

        yield self.driver
        self.driver.quit()

    # 正常场景:货品创建成功
    @allure.title('货品创建成功')
    @allure.severity("Minor")
    def test_item_creation_success(self):
        self.PC.item_creation(ic_data['norms'],ic_data['specs'])


if __name__ == '__main__':

    pytest.main(['test_itemCreation.py', '-s'])  # -s  显示打印
