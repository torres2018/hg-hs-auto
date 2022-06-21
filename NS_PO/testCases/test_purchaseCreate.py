# Author:lilianjun
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from NS_PO.pageObjects.purchaseCreate_page import PurchaseCreatePage
from NS_PO.pageObjects.login_page import LoginPage
from TestData import NsData as ld
import allure

@allure.feature('采购单创建')
@pytest.mark.run(order=3)  # 标签
class TestPurchaseCreate:

    @pytest.fixture(scope='function', autouse=True)
    def login_success(self):
        # 打开浏览器,访问登录页面
        option = webdriver.ChromeOptions()
        option.add_argument(r'user-data-dir=C:\Users\HG\AppData\Local\Google\Chrome\User Data 1')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = 'https://5228089-sb1.app.netsuite.com/app/site/hosting/scriptlet.nl?script=161&deploy=1&compid=5228089_SB1&whence='
        LoginPage().login_success(self.driver, self.url)
        self.PC = PurchaseCreatePage(self.driver)

        yield self.driver
        self.driver.quit()

    # 正常场景:采购单创建
    @allure.title('采购单创建成功')
    @allure.severity("Minor")
    def test_purchase_success(self):
        # 01.库存列表
        self.PC.inventory_list(ld.purchaseCreate_data['good1'])
        # 02.选择PO类型
        self.PC.type_po()
        # 03.购物车详情
        self.PC.shopping_details(ld.purchaseCreate_data['number'])
        # 04.PO购物车列表
        self.PC.shopping_list(ld.purchaseCreate_data['good2'])
        # 05.刷新获取采购单号
        self.PC.refresh_doc_no()
        # 06.点击链接
        self.PC.click_link()
        # 07.PO单编辑
        self.PC.edit_po(ld.purchaseCreate_data['date'])
        # 08.PO单审核
        self.PC.approve_po()

if __name__ == '__main__':

    pytest.main(['test_purchaseCreate.py', '-s'])  # -s  显示打印
