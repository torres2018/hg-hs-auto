from selenium.webdriver.common.by import By

class PurchasePriceLocator:
    # 外部采购价创建流程
    # --------------------------------------------一.查找外部采购价---------------------------------------------------------
    # 01.全局搜索
    global_search = (By.CSS_SELECTOR, '#NS_MENU_ID0-item1 > a')

    # 02.输入货品编码
    import_goods = (By.CSS_SELECTOR, '#Item_NAME')

    # 03.提交
    submit = (By.CSS_SELECTOR, '#submitter')

    # 04.查看
    view = (By.CSS_SELECTOR, '#row0 > td.listtextctr.uir-list-row-cell > a.dottedlink.viewitem')

    # 05.点击外部采购价格
    external_purchase_price = (By.CSS_SELECTOR, '#custom31txt')

    # 06.新建【货品外部采购价格】
    newly_build = (By.CSS_SELECTOR, '#newrecrecmachcustrecord_hg_price_item')

    # --------------------------------------------二.填写外部采购价格单---------------------------------------------------------
    # 01.名称
    name = (By.CSS_SELECTOR, '#name')

    # 02.供应商
    # a.下拉
    drop_down_a = (By.CSS_SELECTOR, '#parent_actionbuttons_custrecord_hg_pric_vend_fs > a:nth-child(2)')
    # b.列表
    list_a = (By.CSS_SELECTOR, '#custrecord_hg_pric_vend_popup_list')
    # c.输入供应商
    inp_supplier = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_a = (By.CSS_SELECTOR, '#Search')
    # e.选择供应商
    cho_supplier = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 03.汇率记录
    # a.下拉
    drop_down_b = (By.CSS_SELECTOR, '#inpt_custrecord_hg_re_record1_arrow')
    # b.选择汇率记录
    exchange_rate = (By.CSS_SELECTOR, '#nl5')

    # 04.报价币种采购价格
    inp_price = (By.CSS_SELECTOR, '#custrecord_hq_gcjj1_formattedValue')

    # 05.开票税点
    # a.下拉
    drop_down_c = (By.CSS_SELECTOR, '#inpt_custrecord_hg_kp_pre2_arrow')
    # b.选择开票税点
    tax_point = (By.CSS_SELECTOR, '#nl12')

    # 06.未含税采购价格保留几位小数
    # a.下拉
    drop_down_d = (By.CSS_SELECTOR, '#inpt_custrecord_hq_sku_price_dot3_arrow')
    # b.未含税采购价格保留几位小数
    decimal_point = (By.CSS_SELECTOR, '#nl28')

    # 07.最终采购价格保留小数位
    # a.下拉
    drop_down_e = (By.CSS_SELECTOR, '#inpt_custrecord_hg_biao_bao_date4_arrow')
    # b.最终采购价格保留小数位
    pur_point = (By.CSS_SELECTOR, '#nl32')

    # 08.是否默认
    # a.下拉
    drop_down_f = (By.CSS_SELECTOR, '#inpt_custrecord_hg_if_defautkes5_arrow')
    # b.是否默认
    default = (By.CSS_SELECTOR, '#nl36')

    # 09.保存
    preservation = (By.CSS_SELECTOR, '#btn_secondarymultibutton_submitter')##btn_secondarymultibutton_submitter

    # 10.弹出框确认

    # ----------------------------------------三.审批货品外部采购价格-------------------------------------------------------
    # 01.外部采购价格
    click_external_price = (By.CSS_SELECTOR, '#custom31txt')

    # 02.选择需要审核的外部采购价[将元素内itemrow0改成itemrow1，则选择下一个]
    check_external_price = (By.CSS_SELECTOR, '#recmachcustrecord_hg_price_itemrow0 > td:nth-child(2) > a')

    # 03.审批通过
    approved = (By.CSS_SELECTOR, '#custpageworkflow344')

    # 04.获取外部采购单号
    get_doc_No = (By.CSS_SELECTOR, '##main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div')

