# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.deliveryNotice_page import DeliveryNoticePage
from NS_PO.pageObjects.login_page import LoginPage
from ddt import ddt,data
import allure

@allure.feature('送货通知单')
@pytest.mark.run(order=5)  # 标签
@ddt
class TestDelivery:

    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        # 打开浏览器,访问登录页面
        Option = webdriver.ChromeOptions()
        Option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        Option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=Option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = 'https://5228089-sb1.app.netsuite.com/app/site/hosting/scriptlet.nl?script=226&deploy=1&compid=5228089_SB1&whence='
        LoginPage().login_success(self.driver, self.url)
        self.DN = DeliveryNoticePage(self.driver)

        # 退出登录
        yield self.driver
        self.driver.quit()

    # 正常场景:送货通知单
    @allure.title('单个送货通知单')
    @allure.severity("Minor")
    def test_delivery_success(self):
        self.DN.delivery()
        # 刷新并获取单号
        self.DN.refresh_odd_no()

    """
    # 正常场景:多组送货通知单
    @allure.title('多个送货通知单')
    @allure.severity("Minor")
    @pytest.mark.parametrize('data', ld.deliveryNotice_datas)  # [pytest参数化方法]
    # @data(*ld.deliveryNotice_datas)   # [ddt的参数化方法]
    def test_delivery_more(self, data):
        self.DN.delivery(data['goods'], data['numbers'])
        #刷新并获取单号
        self.DN.refreshodd()
    """
if __name__ == '__main__':

    pytest.main(['test_deliveryNotice.py', '-s'])  # -s  显示打印


