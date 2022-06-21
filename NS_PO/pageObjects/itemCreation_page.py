from NS_PO.pageLocators.itemCreation_locator import ItemCreationLocator as loc
from Common.BasePage import basePage
import time

class ItemCreationPage(basePage):
    # ----------------------------------------------------01.货品创建流程---------------------------------------------------------
    # 货品创建流程
    def item_creation(self, norms, specs):
        # 01.引用商品
        # a.下拉
        self.wait_eleVisible(loc.drop_down_a, model='下拉')
        self.click_Element(loc.drop_down_a, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_a, model='列表')
        self.click_Element(loc.list_a, model='列表')
        # c.输入商品编码
        time.sleep(1)
        path = r"F:\HS\UI测试-NS\TestData\product.txt"
        product = self.read_data(path)
        self.wait_eleVisible(loc.inp_product, model='输入商品编码')
        self.input_Text(loc.inp_product, text=product, model='输入商品编码')
        time.sleep(3)
        # d.点击搜索
        self.wait_eleVisible(loc.search_a, model='搜索')
        self.click_Element(loc.search_a, model='搜索')
        time.sleep(5)
        # e.选择商品编码
        self.wait_eleVisible(loc.cho_product, model='选择商品编码')
        self.click_Element(loc.cho_product, model='选择商品编码')

        # 02.规格1[同一商品下不能有规格相同的货品]
        # a.下拉
        self.wait_eleVisible(loc.drop_down_b, model='下拉')
        self.click_Element(loc.drop_down_b, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_b, model='列表')
        self.click_Element(loc.list_b, model='列表')
        # c.输入规格1
        self.wait_eleVisible(loc.inp_norms, model='输入规格1')
        self.input_Text(loc.inp_norms, text=norms, model='输入规格1')
        time.sleep(2)
        # d.点击搜索
        self.wait_eleVisible(loc.search_b, model='搜索')
        self.click_Element(loc.search_b, model='搜索')
        time.sleep(3)
        # e.选择规格1
        self.wait_eleVisible(loc.cho_norms, model='选择规格1')
        self.click_Element(loc.cho_norms, model='选择规格1')

        # 03.规格2[同一商品下不能有规格相同的货品]
        # a.下拉
        self.wait_eleVisible(loc.drop_down_c, model='下拉')
        self.click_Element(loc.drop_down_c, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_c, model='列表')
        self.click_Element(loc.list_c, model='列表')
        # c.输入规格2
        self.wait_eleVisible(loc.inp_specs, model='输入规格2')
        self.input_Text(loc.inp_specs, text=specs, model='输入规格2')
        time.sleep(2)
        # d.点击搜索
        self.wait_eleVisible(loc.search_c, model='搜索')
        self.click_Element(loc.search_c, model='搜索')
        time.sleep(3)
        # e.选择规格2
        self.wait_eleVisible(loc.cho_specs, model='选择规格2')
        self.click_Element(loc.cho_specs, model='选择规格2')

        # 04.保存
        # a.下拉
        self.wait_eleVisible(loc.preservation, model='保存')
        self.click_Element(loc.preservation, model='保存')

        # 05.获取货品编码
        time.sleep(2)
        self.wait_eleVisible(loc.item_code, model='货品编码')
        item_code = self.get_Text(loc.item_code, model='货品编码')
        item_path = r'F:\HS\UI测试-NS\TestData\item.txt'
        time.sleep(2)
        self.write_data(item_path, item_code)