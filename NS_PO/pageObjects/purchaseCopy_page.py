from NS_PO.pageLocators.purchaseCopy_locator import PurchaseCopyLocator as loc
from Common.BasePage import basePage
import time

class PurchaseCopyPage(basePage):

    def global_search(self,code):
        time.sleep(3)
        # 01.点击搜索框
        self.wait_eleVisible(loc.click_search, model='搜索')
        self.click_Element(loc.click_search, model='搜索')

        # 02.输入采购单号
        self.wait_eleVisible(loc.inp_code, model='采购单号')
        self.input_Text(loc.inp_code, text=code, model='采购单号')

        # 03.点击提交
        self.wait_eleVisible(loc.submitter, model='提交')
        self.click_Element(loc.submitter, model='提交')

    def copy_po(self):
        time.sleep(3)
        # 01.点击查看
        self.wait_eleVisible(loc.view_code, model='查看')
        self.click_Element(loc.view_code, model='查看')

        # 02.操作[鼠标悬停]
        self.wait_eleVisible(loc.operation_button, model='操作')
        self.move_to_action(loc.operation_button, model='操作')

        # 03.制作副本
        self.wait_eleVisible(loc.make_copy, model='制作副本')
        self.click_Element(loc.make_copy, model='制作副本')

        # 04.切换回原页面
        self.switch_window('default')

        # 05.保存
        self.wait_eleVisible(loc.preservation, model='保存')
        self.click_Element(loc.preservation, model='保存')

    def approve(self):
        time.sleep(2)
        # 确认采购单
        self.wait_eleVisible(loc.adopt, model='确认')
        self.click_Element(loc.adopt, model='确认')
        # 审批采购单
        time.sleep(6)
        self.wait_eleVisible(loc.access, model='审批')
        self.click_Element(loc.access, model='审批')

    def get_po_code(self):
        time.sleep(2)
        # 等待单号出现
        self.wait_eleVisible(loc.get_code, model='采购单号')
        po_code = self.get_Text(loc.get_code, model='采购单号')
        po_path = r'F:\HS\UI测试-NS\TestData\purchase.txt'
        self.write_data(po_path, po_code)



