from NS_PO.pageLocators.purchaseCreate_locator import PurchaseCreateLocator as loc
from Common.BasePage import basePage
import time

class PurchaseCreatePage(basePage):
    # ----------------------------------------------------01.库存列表---------------------------------------------------------
    def inventory_list(self, code):
        time.sleep(3)  # 为什么加强制等待时间？因为隐式等待和显示等待只能设置查找元素和执行命令的超时，对页面加载操作的超时无效。
        # 01.输入货品编码
        self.wait_eleVisible(loc.inp_code, model='货品编码')
        self.input_Text(loc.inp_code, text=code, model='货品编码')

        # 02.点击搜索
        self.wait_eleVisible(loc.click_search, model='搜索')
        self.click_Element(loc.click_search, model='搜索')

        # 03.添加进入购物车
        self.wait_eleVisible(loc.add_to_cart, model='添加进入购物车')
        self.click_Element(loc.add_to_cart, model='添加进入购物车')

        # 04.跳转到新窗口
        self.switch_window('new')

    # ----------------------------------------------------02.选择PO类型-------------------------------------------------------
    def type_po(self):
        time.sleep(3)
        # 01.点击下拉
        self.wait_eleVisible(loc.drop_down_a, model='下拉')
        self.click_Element(loc.drop_down_a, model='下拉')

        # 02.选择PO类型
        self.wait_eleVisible(loc.po_type, model='PO类型')
        self.click_Element(loc.po_type, model='PO类型')

    # ----------------------------------------------------03.购物车详情-------------------------------------------------------
    def shopping_details(self, code):
        time.sleep(3)
        # 01.点击下拉，并选择仓库
        self.wait_eleVisible(loc.drop_down_b, model='下拉')
        self.click_Element(loc.drop_down_b, model='下拉')
        self.wait_eleVisible(loc.wareHouse, model='仓库')
        self.click_Element(loc.wareHouse, model='仓库')

        # 02.采购数量
        self.wait_eleVisible(loc.purchase_quantity, model='采购数量')
        self.input_Text(loc.purchase_quantity, text=code, model='采购数量')

        # 03.结算方式
        self.wait_eleVisible(loc.drop_down_c, model='下拉')
        self.click_Element(loc.drop_down_c, model='下拉')
        self.wait_eleVisible(loc.settlementMethod, model='结算方式')
        self.click_Element(loc.settlementMethod, model='结算方式')

        # 04.供货模式
        self.wait_eleVisible(loc.drop_down_d, model='下拉')
        self.click_Element(loc.drop_down_d, model='下拉')
        self.wait_eleVisible(loc.deliveryOfGoods, model='供货模式')
        self.click_Element(loc.deliveryOfGoods, model='供货模式')

        # 05.添加至PO购物车
        self.wait_eleVisible(loc.submit, model='添加至PO购物车')
        self.click_Element(loc.submit, model='添加至PO购物车')

        # 06.弹框确认
        self.switch_alert()

        # 07.点击进入-购物车列表
        self.wait_eleVisible(loc.preservation, model='购物车列表')
        self.click_Element(loc.preservation, model='购物车列表')

    # ----------------------------------------------------04.PO购物车列表-------------------------------------------------------
    def shopping_list(self, code):
        time.sleep(3)
        # 批量生成PO单
        # 1.输入货品编码
        self.wait_eleVisible(loc.inp_code_a, model='货品编码')
        self.input_Text(loc.inp_code_a, text=code, model='货品编码')

        # 2.点击搜索
        self.wait_eleVisible(loc.search, model='搜索')
        self.click_Element(loc.search, model='搜索')

        # 3.勾选单据
        self.wait_eleVisible(loc.checkImg, model='勾选单据')
        self.click_Element(loc.checkImg, model='勾选单据')

        # 4.生成PO单
        self.wait_eleVisible(loc.generatePo, model='提交')
        self.click_Element(loc.generatePo, model='提交')

    # ----------------------------------------------------05.刷新获取采购单号-------------------------------------------------------
    def refresh_doc_no(self):
        while True:
            flag = self.is_element_exist(loc.poLink)
            if flag:
                self.wait_eleVisible(loc.poLink, model='PO单号')
                self.get_Text(loc.poLink, model='PO单号')
                time.sleep(2)
                break
            else:
                self.wait_eleVisible(loc.refresh, model='刷新')
                self.click_Element(loc.refresh, model='刷新')
                time.sleep(3)
                continue
    # ----------------------------------------------------06.点击单号链接-------------------------------------------------------
    def click_link(self):
        self.click_Element(loc.poLink, model='PO单号链接')

    # ----------------------------------------------------07.PO单编辑【修改交付日期，税收】-------------------------------------------------------
    def edit_po(self,date):
        time.sleep(3)
        # 编辑PO采购单
        self.wait_eleVisible(loc.edit, model='编辑')
        self.click_Element(loc.edit, model='编辑')

        # 是否计算税收
        time.sleep(2)
        self.wait_eleVisible(loc.drop_down_e, model='下拉')
        self.move_to_action(loc.drop_down_e, model='下拉')
        self.click_Element(loc.drop_down_e, model='下拉')
        self.wait_eleVisible(loc.noTax, model='否')
        self.click_Element(loc.noTax, model='否')

        # 交付日期
        self.wait_eleVisible(loc.deliveryDate, model='交付日期')
        self.input_Text(loc.deliveryDate, text=date, model='交付日期')

        # 保存
        time.sleep(2)
        self.wait_eleVisible(loc.preservePo, model='保存')
        self.click_Element(loc.preservePo, model='保存')

    # ----------------------------------------------------08.PO单审核-------------------------------------------------------
    def approve_po(self):
        time.sleep(2)
        # 确认PO采购单
        self.wait_eleVisible(loc.adopt, model='确认')
        self.click_Element(loc.adopt, model='确认')

        # 审批PO采购单
        self.wait_eleVisible(loc.access, model='审核通过')
        self.click_Element(loc.access, model='审核通过')

