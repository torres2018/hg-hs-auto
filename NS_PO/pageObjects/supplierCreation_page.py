from NS_PO.pageLocators.supplierCreation_locator import SupplierCreationLocator as loc
from Common.BasePage import basePage
import time

# 创建供应商流程
class SupplierCreationPage(basePage):
    # 创建供应商流程
    # ----------------------------------------------------01.创建供应商---------------------------------------------------------
    def new_supplier(self):
        # 01.新建供应商
        self.wait_eleVisible(loc.new_supplier, model='新建供应商')
        self.click_Element(loc.new_supplier, model='新建供应商')

    # ----------------------------------------------------02.供应商详情---------------------------------------------------------
    def supplier_details(self, brand, address, register, returns, currency, department, subject):
        time.sleep(3)
        # 01.公司名称
        date_now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        name = 'LLJ专用' + date_now
        self.wait_eleVisible(loc.corporate_name, model='公司名称')
        self.input_Text(loc.corporate_name, text=name, model='公司名称')

        # 02.供应商类别
        time.sleep(2)
        # 下拉
        self.wait_eleVisible(loc.pull_down_a, model='下拉')
        self.click_Element(loc.pull_down_a, model='下拉')
        # 选择供应商类别
        self.wait_eleVisible(loc.supplier_category, model='选择供应商类别')
        self.click_Element(loc.supplier_category, model='选择供应商类别')

        # 03.品牌
        time.sleep(2)
        # a.下拉
        self.wait_eleVisible(loc.drop_down_a, model='下拉')
        self.click_Element(loc.drop_down_a, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_a, model='列表')
        self.click_Element(loc.list_a, model='列表')
        # c.输入品牌
        self.wait_eleVisible(loc.inp_brand, model='输入品牌')
        self.input_Text(loc.inp_brand, text=brand, model='输入品牌')
        time.sleep(2)
        # d.点击搜索
        self.wait_eleVisible(loc.search_a, model='搜索')
        self.click_Element(loc.search_a, model='搜索')
        time.sleep(2)
        # e.选择品牌
        self.wait_eleVisible(loc.cho_brand, model='选择品牌')
        self.click_Element(loc.cho_brand, model='选择品牌')

        # 04.中文地址
        self.wait_eleVisible(loc.chinese_address, model='中文地址')
        self.input_Text(loc.chinese_address, text=address, model='中文地址')

        # 05.注册国家
        # a.下拉
        self.wait_eleVisible(loc.drop_down_b, model='下拉')
        self.click_Element(loc.drop_down_b, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_b, model='列表')
        self.click_Element(loc.list_b, model='列表')
        # c.输入注册国家
        self.wait_eleVisible(loc.inp_country, model='输入注册国家')
        self.input_Text(loc.inp_country, text=register, model='输入注册国家')
        time.sleep(2)
        # d.点击搜索
        self.wait_eleVisible(loc.search_b, model='搜索')
        self.click_Element(loc.search_b, model='搜索')
        time.sleep(2)
        # e.选择注册国家
        self.wait_eleVisible(loc.cho_country, model='选择注册国家')
        self.click_Element(loc.cho_country, model='选择注册国家')

        # 06.供货模式
        # 下拉
        self.wait_eleVisible(loc.pull_down_b, model='下拉')
        self.click_Element(loc.pull_down_b, model='下拉')
        # 选择供货模式
        self.wait_eleVisible(loc.supply_mode, model='选择供货模式')
        self.click_Element(loc.supply_mode, model='选择供货模式')

        # 07.货物来源
        # 下拉
        self.wait_eleVisible(loc.pull_down_c, model='下拉')
        self.click_Element(loc.pull_down_c, model='下拉')
        # 选择货物来源
        self.wait_eleVisible(loc.source_of_goods, model='选择货物来源')
        self.click_Element(loc.source_of_goods, model='选择货物来源')

        # 08.退货地址
        self.wait_eleVisible(loc.return_address, model='退货地址')
        self.input_Text(loc.return_address, text=returns, model='退货地址')

        # 09.结算方式
        # 下拉
        self.wait_eleVisible(loc.pull_down_d, model='下拉')
        self.click_Element(loc.pull_down_d, model='下拉')
        # 选择结算方式
        self.wait_eleVisible(loc.settlement_method, model='选择结算方式')
        self.click_Element(loc.settlement_method, model='选择结算方式')

        # 10.货币
        # a.下拉
        self.wait_eleVisible(loc.drop_down_c, model='下拉')
        self.move_to_action(loc.drop_down_c, model='下拉')
        self.click_Element(loc.drop_down_c, model='下拉')
        # b.输入货币
        self.wait_eleVisible(loc.inp_currency, model='输入货币')
        self.input_Text(loc.inp_currency, text=currency, model='输入货币')
        time.sleep(2)
        # c.点击搜索
        self.wait_eleVisible(loc.search_c, model='搜索')
        self.click_Element(loc.search_c, model='搜索')
        time.sleep(2)
        # d.选择货币
        self.wait_eleVisible(loc.cho_currency, model='选择货币')
        self.click_Element(loc.cho_currency, model='选择货币')
        time.sleep(2)
        # e.更新
        self.wait_eleVisible(loc.update_c, model='更新')
        self.click_Element(loc.update_c, model='更新')

        # 11.部门
        time.sleep(2)
        # a.下拉
        self.wait_eleNoVisible(loc.drop_down_d, model='下拉')
        self.move_to_action(loc.drop_down_d, model='下拉')
        self.click_Element(loc.drop_down_d, model='下拉')
        # b.输入部门
        self.wait_eleVisible(loc.inp_department, model='输入部门')
        self.input_Text(loc.inp_department, text=department, model='输入部门')
        time.sleep(2)
        # c.点击搜索
        self.wait_eleVisible(loc.search_d, model='搜索')
        self.click_Element(loc.search_d, model='搜索')
        time.sleep(2)
        # d.选择部门
        self.wait_eleVisible(loc.cho_department, model='选择部门')
        self.click_Element(loc.cho_department, model='选择部门')
        time.sleep(2)
        # e.更新
        self.wait_eleVisible(loc.update_d, model='更新')
        self.click_Element(loc.update_d, model='更新')

        # 12.收件人
        self.wait_eleVisible(loc.receiver, model='收件人')
        self.input_Text(loc.receiver, text='李连军', model='收件人')

        # 13.城市
        self.wait_eleVisible(loc.city, model='城市')
        self.input_Text(loc.city, text='上海', model='城市')

        # 14.地址
        self.wait_eleVisible(loc.location, model='地址')
        self.input_Text(loc.location, text='南翔', model='地址')

        # 15.州、省
        self.wait_eleVisible(loc.province, model='州、省')
        self.input_Text(loc.province, text='祥和雅苑', model='州、省')

        # 16.邮编
        self.wait_eleVisible(loc.zip_code, model='邮编')
        self.input_Text(loc.zip_code, text='66666666', model='邮编')

        # 17.电话
        self.wait_eleVisible(loc.phone_number, model='电话')
        self.input_Text(loc.phone_number, text='15601608610', model='电话')

        # 18.收件国家
        # a.下拉
        self.wait_eleVisible(loc.drop_down_e, model='下拉')
        self.click_Element(loc.drop_down_e, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_e, model='列表')
        self.click_Element(loc.list_e, model='列表')
        # c.输入收件国家
        self.wait_eleVisible(loc.inp_nation, model='输入收件国家')
        self.input_Text(loc.inp_nation, text='中国', model='输入收件国家')
        time.sleep(2)
        # d.点击搜索
        self.wait_eleVisible(loc.search_e, model='搜索')
        self.click_Element(loc.search_e, model='搜索')
        time.sleep(2)
        # e.选择注册国家
        self.wait_eleVisible(loc.cho_nation, model='选择收件国家')
        self.click_Element(loc.cho_nation, model='选择收件国家')

        # 19.采购主体
        time.sleep(2)
        self.wait_eleVisible(loc.inp_subject, model='采购主体')
        self.input_Text(loc.inp_subject, text=subject, model='采购主体')

        # 20.统一计量单位
        # a.下拉
        self.wait_eleVisible(loc.drop_down_f, model='下拉')
        self.click_Element(loc.drop_down_f, model='下拉')
        # b.列表
        self.wait_eleVisible(loc.list_f, model='列表')
        self.click_Element(loc.list_f, model='列表')
        # c.输入统一计量单位
        self.wait_eleVisible(loc.inp_unit, model='输入统一计量单位')
        self.input_Text(loc.inp_unit, text='个', model='输入统一计量单位')
        time.sleep(2)
        # d.点击搜索
        self.wait_eleVisible(loc.search_f, model='搜索')
        self.click_Element(loc.search_f, model='搜索')
        time.sleep(2)
        # e.选择统一计量单位
        self.wait_eleVisible(loc.cho_unit, model='选择统一计量单位')
        self.click_Element(loc.cho_unit, model='选择统一计量单位')
        time.sleep(2)


        """
        # a.下拉
        self.wait_eleVisible(loc.drop_down_g, model='下拉')
        self.move_to_action(loc.drop_down_g, model='下拉')
        self.click_Element(loc.drop_down_g, model='下拉')
        time.sleep(1)
        # b.列表
        self.wait_eleVisible(loc.list_g, model='列表')
        self.move_to_action(loc.list_g, model='下拉')
        self.click_Element(loc.list_g, model='列表')
        # c.输入采购主体
        self.wait_eleVisible(loc.inp_subject, model='输入采购主体')
        self.input_Text(loc.inp_subject, text=subject, model='输入采购主体')
        time.sleep(3)
        # d.点击搜索
        self.wait_eleVisible(loc.search_g, model='搜索')
        self.click_Element(loc.search_g, model='搜索')
        time.sleep(3)
        # e.选择采购主体
        self.wait_eleVisible(loc.cho_subject, model='选择采购主体')
        self.click_Element(loc.cho_subject, model='选择采购主体')
 

        # 21.返回原default
        self.switch_window('default')
        time.sleep(2)
       """

        # 22.保存
        self.wait_eleVisible(loc.submitter, model='保存')
        self.click_Element(loc.submitter, model='保存')

        # 23.获取供应商编码
        time.sleep(2)
        self.wait_eleVisible(loc.supplier_code, model='获取供应商编码')
        self.get_Text(loc.supplier_code, model='获取供应商编码')

