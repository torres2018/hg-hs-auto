from NS_PO.pageLocators.inventoryAdjustment_locator import InventoryAdjustmentLocator as loc
from Common.BasePage import basePage
import time

class InventoryAdjustmentPage(basePage):
    # ----------------------------------------------------01.库存调整单流程---------------------------------------------------------
    # 库存调整单流程
    def inventory_adjustment(self, company, product, warehouse, quantity):
        time.sleep(5)
        # 1.附属公司
        # a.下拉
        self.wait_eleVisible(loc.drop_down_a, model='下拉')
        self.click_Element(loc.drop_down_a, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_a, model='列表')
        self.click_Element(loc.list_a, model='列表')
        # c.输入子公司
        self.wait_eleVisible(loc.inp_company, model='输入子公司')
        self.input_Text(loc.inp_company, text=company, model='输入子公司')
        time.sleep(3)
        # d.点击搜索
        self.wait_eleVisible(loc.search_a, model='搜索')
        self.click_Element(loc.search_a, model='搜索')
        time.sleep(3)
        # e.选择子公司
        self.wait_eleVisible(loc.cho_company, model='选择子公司')
        self.click_Element(loc.cho_company, model='选择子公司')

        # 2.调整科目
        # a.下拉
        time.sleep(3)
        self.wait_eleVisible(loc.drop_down_b, model='下拉')
        self.click_Element(loc.drop_down_b, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_b, model='列表')
        self.click_Element(loc.list_b, model='列表')
        time.sleep(2)
        # e.选择科目
        self.wait_eleVisible(loc.cho_course, model='科目')
        self.click_Element(loc.cho_course, model='科目')

        # 3.货品【PN0000000057161】
        # a.下拉
        time.sleep(3)
        self.wait_eleVisible(loc.drop_down_c, model='下拉')
        self.click_Element(loc.drop_down_c, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_c, model='列表')
        self.click_Element(loc.list_c, model='列表')
        # c.输入货品
        self.wait_eleVisible(loc.inp_product, model='输入货品')
        self.input_Text(loc.inp_product, text=product, model='输入货品')
        time.sleep(3)
        # d.点击搜索
        self.wait_eleVisible(loc.search_c, model='搜索')
        self.click_Element(loc.search_c, model='搜索')
        time.sleep(5)
        # e.选择货品
        self.wait_eleVisible(loc.cho_product, model='选择货品')
        self.click_Element(loc.cho_product, model='选择货品')

        # 4.地点[深圳仓-新香港公司]
        # 点击一下
        time.sleep(3)
        self.wait_eleVisible(loc.click_one, model='点击一下')
        self.click_Element(loc.click_one, model='点击一下')
        # a.下拉
        self.wait_eleVisible(loc.drop_down_d, model='下拉')
        self.click_Element(loc.drop_down_d, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_d, model='列表')
        self.click_Element(loc.list_d, model='列表')
        # c.输入仓库
        self.wait_eleVisible(loc.inp_warehouse, model='输入仓库')
        self.input_Text(loc.inp_warehouse, text=warehouse, model='输入仓库')
        time.sleep(3)
        # d.点击搜索
        self.wait_eleVisible(loc.search_d, model='搜索')
        self.click_Element(loc.search_d, model='搜索')
        time.sleep(3)
        # e.选择仓库
        self.wait_eleVisible(loc.cho_warehouse, model='选择仓库')
        self.click_Element(loc.cho_warehouse, model='选择仓库')

        # 5.调整数量
        # 点击一下
        time.sleep(3)
        self.wait_eleVisible(loc.click_two, model='点击一下')
        self.click_Element(loc.click_two, model='点击一下')
        # a.调整数量
        self.wait_eleVisible(loc.inp_quantity, model='调整数量')
        self.input_Text(loc.inp_quantity, text=quantity, model='输入仓库')

        # 6.添加
        time.sleep(3)
        self.wait_eleVisible(loc.add_to, model='添加')
        self.click_Element(loc.add_to, model='添加')

        # 7.保存
        time.sleep(2)
        self.wait_eleVisible(loc.preservation, model='保存')
        self.click_Element(loc.preservation, model='保存')

        # 8.库存调整单号
        time.sleep(2)
        self.wait_eleVisible(loc.odd_numbers, model='库存调整单号')
        self.get_Text(loc.odd_numbers, model='库存调整单号')

