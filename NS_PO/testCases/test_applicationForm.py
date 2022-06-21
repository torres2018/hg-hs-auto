# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.applicationForm_page import ApplicationFormPage
from NS_PO.pageObjects.login_page import LoginPage
from TestData import NsData as ld
import allure

ar_date = ld.applicationForm_data

@allure.feature('AR申请单流程')
@pytest.mark.run(order=2)  # 标签
class TestApplicationForm:
    """
        这是pytest中的预置函数定义的配置文件：
        scope参数：标记方法的作用域。有4个可选值：function（默认，函数）、class（类）、module（模块）、package/session（包）
            function：每个函数或方法都会调用
            class：每个类只调用1次
            module：每个模块只调用1次
            session：多个模块调用1次，通常写在conftest【文件名写死，必须这么写】中
    """
    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        # 打开浏览器,访问登录页面
        Option = webdriver.ChromeOptions()
        Option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        Option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=Option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = f"https://5228089-sb1.app.netsuite.com/app/common/custom/custrecordentry.nl?rectype=195"
        LoginPage().login_success(self.driver, self.url)
        self.PC = ApplicationFormPage(self.driver)

        yield self.driver
        self.driver.quit()

    # 正常场景:AR申请单增加与冲减
    @allure.title('AR余额增加与冲减')
    @allure.severity("Minor")
    def test_application_form(self):
        # 01.AR申请单增加
        self.PC.ar_application_process(ar_date['customer'], ar_date['money'], ar_date['date'], ar_date['explain'])
        # 02.AR申请单反向冲减
        self.PC.ar_application_offset()

    """  
    # 正常场景:AR申请单正向增加
    @allure.title('AR余额增加')
    @allure.severity("Minor")
    def test_application_form(self):
        # 01.AR申请单增加
        self.PC.ar_application_process(ar_date['customer'], ar_date['money'], ar_date['date'], ar_date['explain'])
    """

if __name__ == '__main__':

    pytest.main(['test_applicationForm.py', '-s'])  # -s  显示打印
