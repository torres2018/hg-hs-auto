from NS_PO.pageLocators.purchasePrice_locator import PurchasePriceLocator as loc
from Common.BasePage import basePage
import time

# 外部采购价创建流程
class PurchasePricePage(basePage):
    # --------------------------------------------一.查找外部采购价---------------------------------------------------------
    def global_search(self):
        time.sleep(3)
        # 01.全局搜索
        self.wait_eleVisible(loc.global_search, model='全局搜索')
        self.click_Element(loc.global_search, model='全局搜索')

        # 02.输入货品编码
        time.sleep(1)
        item_path = r'F:\HS\UI测试-NS\TestData\item.txt'
        item = self.read_data(item_path)
        self.wait_eleVisible(loc.import_goods, model='货品编码')
        self.input_Text(loc.import_goods, text=item, model='货品编码')

        # 03.提交
        self.wait_eleVisible(loc.submit, model='提交')
        self.click_Element(loc.submit, model='提交')

        # 04.查看
        time.sleep(2)
        self.wait_eleVisible(loc.view, model='查看')
        self.click_Element(loc.view, model='查看')

        # 05.点击外部采购价格
        self.wait_eleVisible(loc.external_purchase_price, model='查看外部采购价格')
        self.click_Element(loc.external_purchase_price, model='查看外部采购价格')

        # 06.新建【货品外部采购价格】
        self.wait_eleVisible(loc.newly_build, model='新建【货品外部采购价格】')
        self.click_Element(loc.newly_build, model='新建【货品外部采购价格】')

    # --------------------------------------------二.填写外部采购价格单---------------------------------------------------------
    def fill_in_documents(self, supplier, price):
        time.sleep(5)
        # 01.名称
        str1 = 'LI'
        str2 = str(int(time.time()))
        pro_name = str1 + str2
        self.wait_eleVisible(loc.name, model='名称')
        self.input_Text(loc.name, text=pro_name, model='名称')

        # 02.供应商
        # a.下拉
        self.wait_eleVisible(loc.drop_down_a, model='下拉')
        self.click_Element(loc.drop_down_a, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_a, model='列表')
        self.click_Element(loc.list_a, model='列表')
        # c.输入供应商
        self.wait_eleVisible(loc.inp_supplier, model='输入供应商')
        self.input_Text(loc.inp_supplier, text=supplier, model='输入供应商')
        time.sleep(3)
        # d.点击搜索
        self.wait_eleVisible(loc.search_a, model='搜索')
        self.click_Element(loc.search_a, model='搜索')
        time.sleep(5)
        # e.选择供应商
        self.wait_eleVisible(loc.cho_supplier, model='选择供应商')
        self.click_Element(loc.cho_supplier, model='选择供应商')

        # 03.汇率记录
        # a.下拉
        self.wait_eleVisible(loc.drop_down_b, model='下拉')
        self.click_Element(loc.drop_down_b, model='下拉')
        # b.选择汇率记录
        self.wait_eleVisible(loc.exchange_rate, model='选择汇率记录')
        self.click_Element(loc.exchange_rate, model='选择汇率记录')

        # 04.报价币种采购价格
        self.wait_eleVisible(loc.inp_price, model='选择汇率记录')
        self.input_Text(loc.inp_price, text=price, model='输入供应商')

        # 05.开票税点
        # a.下拉
        self.wait_eleVisible(loc.drop_down_c, model='下拉')
        self.click_Element(loc.drop_down_c, model='下拉')
        # b.选择开票税点
        self.wait_eleVisible(loc.tax_point, model='选择开票税点')
        self.click_Element(loc.tax_point, model='选择开票税点')

        # 06.未含税采购价格保留几位小数
        # a.下拉
        self.wait_eleVisible(loc.drop_down_d, model='下拉')
        self.click_Element(loc.drop_down_d, model='下拉')
        # b.选择小数点
        self.wait_eleVisible(loc.decimal_point, model='选择小数点')
        self.click_Element(loc.decimal_point, model='选择小数点')

        # 07.最终采购价格保留小数位
        # a.下拉
        self.wait_eleVisible(loc.drop_down_e, model='下拉')
        self.click_Element(loc.drop_down_e, model='下拉')
        # b.保留小数位
        self.wait_eleVisible(loc.pur_point, model='保留小数位')
        self.click_Element(loc.pur_point, model='保留小数位')

        # 08.是否默认
        # a.下拉
        self.wait_eleVisible(loc.drop_down_f, model='下拉')
        self.click_Element(loc.drop_down_f, model='下拉')
        # b.是否默认
        self.wait_eleVisible(loc.default, model='是否默认')
        self.click_Element(loc.default, model='是否默认')

        # 09.保存
        time.sleep(2)
        self.wait_eleVisible(loc.preservation, model='保存')
        self.click_Element(loc.preservation, model='保存')

        # 10.弹出框确认
        self.switch_alert()

        # ----------------------------------------三.审批货品外部采购价格-------------------------------------------------------
    def approval_document(self):
        time.sleep(3)
        # 01.外部采购价格
        self.wait_eleVisible(loc.click_external_price, model='外部采购价格')
        self.click_Element(loc.click_external_price, model='外部采购价格')

        # 02.选择需要审核的外部采购价[将元素内itemrow0改成itemrow1，则选择下一个]
        self.wait_eleVisible(loc.check_external_price, model='选择需要审核的外部采购价')
        self.click_Element(loc.check_external_price, model='选择需要审核的外部采购价')

        # 03.审批通过
        self.wait_eleVisible(loc.approved, model='审批通过')
        self.click_Element(loc.approved, model='审批通过')
