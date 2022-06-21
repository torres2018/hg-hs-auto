from selenium.webdriver.common.by import By

class PurchaseCopyLocator:
    # ----------------------------------------------------01.全局搜索-------------------------------------------------
    # 01.全局搜索
    click_search = (By.CSS_SELECTOR, '#NS_MENU_ID0-item1 > a')

    # 02.输入采购单号[PO000013480(VD000003071 LLJ-领用专用)]  [PO000013491(VD000002760 深圳市米茄科技有限公司)]
    inp_code = (By.CSS_SELECTOR, '#Transaction_NUMBERTEXT')

    # 03.提交
    submitter = (By.CSS_SELECTOR, '#secondarysubmitter')

    # ----------------------------------------------------02.采购单复制-------------------------------------------------
    # 04.点击查看
    view_code = (By.CSS_SELECTOR, '#row0 > td.listtextctr.uir-list-row-cell > a.dottedlink.viewitem')

    # 05.操作-制作副本
    operation_button = (By.CSS_SELECTOR, '#spn_ACTIONMENU_d1 > span.pgm_bg > a')
    make_copy = (By.CSS_SELECTOR, '#nl2 > a > span')

    # 06.返回原default

    # 07.保存
    preservation = (By.CSS_SELECTOR, '#btn_secondarymultibutton_submitter')

    # ----------------------------------------------------03.审核采购单-------------------------------------------------
    # 08.审批确认
    adopt = (By.CSS_SELECTOR, '#custpage_purchase_order')

    # 08.审批通过
    access = (By.CSS_SELECTOR, '#custpageworkflow398')

    # ----------------------------------------------------04.获取采购单号-------------------------------------------------

    # 09.获取采购单号
    get_code = (By.CSS_SELECTOR, '#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div.uir-record-id')

