from NS_PO.pageLocators.deliveryNotice_locator import DeliveryNoticeLocator as loc
from Common.BasePage import basePage
import time
from datetime import date


class DeliveryNoticePage(basePage):

    # 送货通知单
    def delivery(self):
        path = r"F:\HS\UI测试-NS\TestData\purchase.txt"
        code = self.read_data(path)
        # 1.采购单号
        self.wait_eleVisible(loc.goods_input, model='采购单号')
        self.input_Text(loc.goods_input, text=code, model='采购单号')

        # 2.搜索
        time.sleep(2)
        self.wait_eleVisible(loc.search, model='搜索')
        self.click_Element(loc.search, model='搜索')

        # 3.日期
        self.wait_eleVisible(loc.today, model='日期')
        self.input_Text(loc.today, text=str(date.today()), model='日期')

        # 4.输入发货数量
        self.wait_eleVisible(loc.quantity, model='清除发货数量')
        self.clean_Input_Text(loc.quantity, model='清除发货数量')
        self.input_Text(loc.quantity, text=100, model='重新输入发货数量')

        # 5.提交
        self.wait_eleVisible(loc.submit, model='提交')
        self.click_Element(loc.submit, model='提交')
        time.sleep(6)

    # 刷新页面
    def refresh_odd_no(self):
        while True:
            flag = self.is_element_exist(loc.oddtext)
            if flag:
                self.wait_eleVisible(loc.oddtext, model='送货通知单号')
                self.get_Text(loc.oddtext, model='送货通知单号')
                time.sleep(2)
                break
            else:
                self.wait_eleVisible(loc.refresh, model='刷新')
                self.click_Element(loc.refresh, model='刷新')
                time.sleep(3)
                continue

