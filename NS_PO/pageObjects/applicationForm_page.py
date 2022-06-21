from NS_PO.pageLocators.applicationForm_locator import ApplicationFormLocator as loc
from Common.BasePage import basePage
import time

class ApplicationFormPage(basePage):
    # ----------------------------------------------------01.客户AR申请单[增加额度]---------------------------------------------------------
    # 客户AR申请单流程
    def ar_application_process(self, customer, money, date, explain):
        time.sleep(5)
        # 01.客户名称
        self.wait_eleVisible(loc.customer_name, model='客户名称')
        self.input_Text(loc.customer_name,text=customer, model='客户名称')
        time.sleep(3)

        # 02.申请类型【信用额度发货】
        self.wait_eleVisible(loc.application_type, model='申请类型')
        self.click_Element(loc.application_type, model='申请类型')
        self.wait_eleVisible(loc.credit_line_shipment, model='信用额度发货')
        self.click_Element(loc.credit_line_shipment, model='信用额度发货')

        # 03.申请金额
        self.wait_eleVisible(loc.application_amount, model='申请金额')
        self.input_Text(loc.application_amount, text=money, model='申请金额')

        # 04.到期时间
        self.wait_eleVisible(loc.expiration_time, model='到期时间')
        self.input_Text(loc.expiration_time, text=date, model='到期时间')

        # 05.备注说明【富文本】
        time.sleep(3)
        # self.switch_iframe('cke_custrecord_hg_cus_remarks')#原ID:ext-gen57
        self.wait_eleVisible(loc.remarks, model='备注说明')
        self.input_Text(loc.remarks, text=explain, model='备注说明')
        time.sleep(2)
        self.switch_window('default')

        # 06.保存
        self.wait_eleVisible(loc.preservation, model='保存')
        self.click_Element(loc.preservation, model='保存')

        # 07.提交审批
        self.wait_eleVisible(loc.submit, model='提交审批')
        self.click_Element(loc.submit, model='提交审批')

        # 08.审批确认
        self.wait_eleVisible(loc.approval, model='审批确认')
        self.click_Element(loc.approval, model='审批确认')

        # 09.再次审批确认
        self.wait_eleVisible(loc.confirmation, model='再次审批确认')
        self.click_Element(loc.confirmation, model='再次审批确认')

        # 10.标记已冲减
        self.wait_eleVisible(loc.mark_offset, model='标记已冲减')
        self.click_Element(loc.mark_offset, model='标记已冲减')

        # 11.获取AR申请单号
        self.wait_eleVisible(loc.odd_numbers, model='AR申请单号')
        self.get_Text(loc.odd_numbers, model='AR申请单号')

    # --------------------------02.已冲减AR申请单[清空额度，审批完成才能重新申请AR---------------------------------------------------
    def ar_application_offset(self):
        time.sleep(5)
        # 1.事务处理
        self.wait_eleVisible(loc.transaction_processing, model='事务处理')
        self.move_to_action(loc.transaction_processing, model='事务处理')

        # 02.销售[鼠标悬停]
        self.wait_eleVisible(loc.sale, model='销售')
        self.move_to_action(loc.sale, model='销售')

        # 03.客户AR申请单
        self.wait_eleVisible(loc.ar_application_form, model='客户AR申请单')
        self.click_Element(loc.ar_application_form, model='客户AR申请单')

        # 04.点击查看
        self.wait_eleVisible(loc.see, model='查看')
        self.click_Element(loc.see, model='查看')

        # 05.保存
        self.wait_eleVisible(loc.confirm_adjustment, model='保存')
        self.click_Element(loc.confirm_adjustment, model='保存')



