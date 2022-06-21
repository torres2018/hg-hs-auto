from NS_PO.pageLocators.productCreation_locator import ProductCreationLocator as loc
from Common.BasePage import basePage
import time

class ProductCreationPage(basePage):
    # ----------------------------------------------------01.商品创建流程---------------------------------------------------------
    # 商品创建流程
    def product_creation(self, brand, norms, specs, date, supplier, unit):
        time.sleep(5)
        # 01.商品名称
        str1 = 'test'
        str2 = str(int(time.time()))
        pro_name = str1 + str2
        self.input_Text(loc.trade_name, text=pro_name, model='商品名称')

        # 02.采购名称
        str3 = 'purchase'
        str4 = str(int(time.time()))
        pur_name = str3 + str4
        self.input_Text(loc.purchase_name, text=pur_name, model='采购名称')

        # 03.品牌
        # a.下拉
        self.wait_eleVisible(loc.drop_down_a, model='下拉')
        self.click_Element(loc.drop_down_a, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_a, model='列表')
        self.click_Element(loc.list_a, model='列表')
        # c.输入商品名称
        self.wait_eleVisible(loc.inp_brand, model='输入品牌')
        self.input_Text(loc.inp_brand, text=brand, model='输入品牌')
        time.sleep(1)
        # d.点击搜索
        self.wait_eleVisible(loc.search_a, model='搜索')
        self.click_Element(loc.search_a, model='搜索')
        time.sleep(3)
        # e.选择商品名称
        self.wait_eleVisible(loc.cho_brand, model='选择品牌')
        self.click_Element(loc.cho_brand, model='选择品牌')

        # 04.规格1
        # a.下拉
        self.wait_eleVisible(loc.drop_down_b, model='下拉')
        self.click_Element(loc.drop_down_b, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_b, model='列表')
        self.click_Element(loc.list_b, model='列表')
        # c.输入规格1
        self.wait_eleVisible(loc.inp_specifications_b, model='输入规格1')
        self.input_Text(loc.inp_specifications_b, text=norms, model='输入规格1')
        time.sleep(2)
        # d.点击搜索
        self.wait_eleVisible(loc.search_b, model='搜索')
        self.click_Element(loc.search_b, model='搜索')
        time.sleep(3)
        # e.选择规格1
        self.wait_eleVisible(loc.cho_specifications_b, model='选择规格1')
        self.click_Element(loc.cho_specifications_b, model='选择规格1')

        # 05.规格2
        # a.下拉
        self.wait_eleVisible(loc.drop_down_c, model='下拉')
        self.click_Element(loc.drop_down_c, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_c, model='列表')
        self.click_Element(loc.list_c, model='列表')
        # c.输入规格2
        self.wait_eleVisible(loc.inp_specifications_c, model='输入规格2')
        self.input_Text(loc.inp_specifications_c, text=specs, model='输入规格2')
        time.sleep(2)
        # d.点击搜索
        self.wait_eleVisible(loc.search_c, model='搜索')
        self.click_Element(loc.search_c, model='搜索')
        time.sleep(3)
        # e.选择规格2
        self.wait_eleVisible(loc.cho_specifications_c, model='选择规格2')
        self.click_Element(loc.cho_specifications_c, model='选择规格2')

        # 06.报关类型
        # 下拉
        self.wait_eleVisible(loc.customs_declaration_type, model='下拉')
        self.click_Element(loc.customs_declaration_type, model='下拉')
        # 选择报关
        self.wait_eleVisible(loc.qa_type, model='报关类型')
        self.click_Element(loc.qa_type, model='报关类型')

        # 07.进销性质
        # 下拉
        self.wait_eleVisible(loc.nature_list, model='下拉')
        self.click_Element(loc.nature_list, model='下拉')
        # 选择进销性质
        self.wait_eleVisible(loc.nature, model='进销性质')
        self.click_Element(loc.nature, model='进销性质')

        # 08.交期
        self.wait_eleVisible(loc.delivery_date, model='下拉')
        self.input_Text(loc.delivery_date, text=date, model='下拉')

        # 09.类别
        # 下拉
        self.wait_eleVisible(loc.category_list, model='下拉')
        self.click_Element(loc.category_list, model='下拉')
        # 选择类别
        self.wait_eleVisible(loc.category, model='类别')
        self.click_Element(loc.category, model='类别')

        # 10.是否为铺货
        # 下拉
        self.wait_eleVisible(loc.distribution_list, model='下拉')
        self.click_Element(loc.distribution_list, model='下拉')
        # 选择是否为铺货
        self.wait_eleVisible(loc.distribution, model='是否为铺货')
        self.click_Element(loc.distribution, model='是否为铺货')

        # 11.主供应商
        # a.下拉
        self.wait_eleVisible(loc.drop_down_d, model='下拉')
        self.click_Element(loc.drop_down_d, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_d, model='列表')
        self.click_Element(loc.list_d, model='列表')
        # c.输入主供应商
        self.wait_eleVisible(loc.inp_supplier, model='输入主供应商')
        self.input_Text(loc.inp_supplier, text=supplier, model='输入主供应商')
        time.sleep(1)
        # d.点击搜索
        self.wait_eleVisible(loc.search_d, model='搜索')
        self.click_Element(loc.search_d, model='搜索')
        time.sleep(3)
        # e.选择主供应商
        self.wait_eleVisible(loc.cho_supplier, model='选择主供应商')
        self.click_Element(loc.cho_supplier, model='选择主供应商')

        # 12.单位
        # a.下拉
        self.wait_eleVisible(loc.drop_down_e, model='下拉')
        self.click_Element(loc.drop_down_e, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_e, model='列表')
        self.click_Element(loc.list_e, model='列表')
        # c.输入单位
        self.wait_eleVisible(loc.inp_unit, model='输入单位')
        self.input_Text(loc.inp_unit, text=unit, model='输入单位')
        time.sleep(1)
        # d.点击搜索
        self.wait_eleVisible(loc.search_e, model='搜索')
        self.click_Element(loc.search_e, model='搜索')
        time.sleep(3)
        # e.选择单位
        self.wait_eleVisible(loc.cho_unit, model='选择单位')
        self.click_Element(loc.cho_unit, model='选择单位')

        # 13.库存分类·一级
        # 下拉
        self.wait_eleVisible(loc.inventory_classification_a, model='下拉')
        self.click_Element(loc.inventory_classification_a, model='下拉')
        # 选择库存分类·一级
        self.wait_eleVisible(loc.class_a, model='库存分类·一级')
        self.click_Element(loc.class_a, model='库存分类·一级')

        # 14.库存分类·二级
        time.sleep(2)
        # 下拉
        self.wait_eleVisible(loc.inventory_classification_b, model='下拉')
        self.click_Element(loc.inventory_classification_b, model='下拉')
        # 选择库存分类·二级
        self.wait_eleVisible(loc.class_b, model='库存分类·二级')
        self.click_Element(loc.class_b, model='库存分类·二级')

        # 15.部门
        time.sleep(3)
        # 下拉
        self.wait_eleNoVisible(loc.department_list, model='下拉')
        self.move_to_action(loc.department_list, model='下拉')
        self.click_Element(loc.department_list, model='下拉')
        # 选择部门
        self.wait_eleVisible(loc.department, model='部门')
        self.click_Element(loc.department, model='部门')
        # 更新
        self.wait_eleVisible(loc.update, model='更新')
        self.click_Element(loc.update, model='更新')

        # 16.保存
        time.sleep(2)
        self.wait_eleVisible(loc.preservation, model='保存')
        self.click_Element(loc.preservation, model='保存')

        # 17.获取商品编码
        time.sleep(2)
        self.wait_eleVisible(loc.commodity_code, model='商品编码')
        pd_code = self.get_Text(loc.commodity_code, model='商品编码')
        pd_path = r'F:\HS\UI测试-NS\TestData\product.txt'
        time.sleep(2)
        self.write_data(pd_path, pd_code)



