# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.purchaseCopy_page import PurchaseCopyPage
from NS_PO.pageObjects.login_page import LoginPage
from TestData import NsData as ld
import allure

@allure.feature('采购单制作副本')
@pytest.mark.run(order=4)  # 标签
class TestPurchaseCopy:

    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        # 打开浏览器,访问登录页面
        Option = webdriver.ChromeOptions()
        Option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        Option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=Option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = 'https://5228089-sb1.app.netsuite.com/app/accounting/transactions/transactionlist.nl?Transaction_TYPE=PurchOrd&whence='
        LoginPage().login_success(self.driver, self.url)
        self.PC = PurchaseCopyPage(self.driver)

        yield self.driver
        self.driver.quit()

    # 正常场景:采购单创建
    @allure.title('采购单复制成功')
    @allure.severity("Minor")
    def test_purchase_success(self):
        # 01.全局搜索
        self.PC.global_search(ld.purchaseCopy_data['code'])
        # 02.采购单复制
        self.PC.copy_po()
        # 03.审核采购单
        self.PC.approve()
        # 04.获取PO单号
        self.PC.get_po_code()

if __name__ == '__main__':

    pytest.main(['test_purchaseCopy.py', '-s'])  # -s  显示打印
