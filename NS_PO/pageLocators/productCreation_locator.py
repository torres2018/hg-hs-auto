from selenium.webdriver.common.by import By

class ProductCreationLocator:
    # 商品创建流程
    # ----------------------------------------------------一.商品创建---------------------------------------------------------
    # 01.商品名称
    trade_name = (By.CSS_SELECTOR, '#altname')

    # 02.采购名称
    purchase_name = (By.CSS_SELECTOR, '#custrecord_hq_spu_p_name')

    # 03.品牌
    # a.下拉
    drop_down_a = (By.CSS_SELECTOR, '#parent_actionbuttons_custrecord_hq_spu_bland_fs > a:nth-child(2)')
    # b.列表
    list_a = (By.CSS_SELECTOR, '#custrecord_hq_spu_bland_popup_list')
    # c.输入品牌
    inp_brand = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_a = (By.CSS_SELECTOR, '#Search')
    # e.选择品牌
    cho_brand = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 04.规格1
    # a.下拉
    drop_down_b = (By.CSS_SELECTOR, '#parent_actionbuttons_custrecord_hg_spu_soec_1_fs > a:nth-child(2)')
    # b.列表
    list_b = (By.CSS_SELECTOR, '#custrecord_hg_spu_soec_1_popup_list')
    # c.输入规格1
    inp_specifications_b = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_b = (By.CSS_SELECTOR, '#Search')
    # e.选择规格1
    cho_specifications_b = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 05.规格2
    # a.下拉
    drop_down_c = (By.CSS_SELECTOR, '#parent_actionbuttons_custrecord_hg_spu_spec_2_fs > a:nth-child(2)')
    # b.列表
    list_c = (By.CSS_SELECTOR, '#custrecord_hg_spu_spec_2_popup_list')
    # c.输入规格2
    inp_specifications_c = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_c = (By.CSS_SELECTOR, '#Search')
    # e.选择规格2
    cho_specifications_c = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 06.报关类型
    customs_declaration_type = (By.CSS_SELECTOR, '#inpt_custrecord_hq_bglx2_arrow')
    qa_type = (By.CSS_SELECTOR, '#nl3')

    # 07.进销性质
    nature_list = (By.CSS_SELECTOR, '#inpt_custrecord_hq_jxxx13_arrow')
    nature = (By.CSS_SELECTOR, '#nl8')

    # 08.交期
    delivery_date = (By.CSS_SELECTOR, '#custrecord_hq_jiaoqi')

    # 09.类别
    category_list = (By.CSS_SELECTOR, '#inpt_custrecord_hg_d_cd7_arrow')
    category = (By.CSS_SELECTOR, '#nl16')

    # 10.是否为铺货
    distribution_list = (By.CSS_SELECTOR, '#inpt_custrecord_hg_if_pu_df8_arrow')
    distribution = (By.CSS_SELECTOR, '#nl19')

    # 11.主供应商
    # a.下拉
    drop_down_d = (By.CSS_SELECTOR, '#parent_actionbuttons_custrecord_hg_mubd_vend_rf_fs > a:nth-child(2)')
    # b.列表
    list_d = (By.CSS_SELECTOR, '#custrecord_hg_mubd_vend_rf_popup_list')
    # c.输入主供应商
    inp_supplier = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_d = (By.CSS_SELECTOR, '#Search')
    # e.选择主供应商
    cho_supplier = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 12.单位
    # a.下拉
    drop_down_e = (By.CSS_SELECTOR, '#parent_actionbuttons_custrecord_hg_spu_unit_fs > a:nth-child(2)')
    # b.列表
    list_e = (By.CSS_SELECTOR, '#custrecord_hg_spu_unit_popup_list')
    # c.输入单位
    inp_unit = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_e = (By.CSS_SELECTOR, '#Search')
    # e.选择单位
    cho_unit = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 13.库存分类·一级
    inventory_classification_a = (By.CSS_SELECTOR, '#inpt_custrecord_hg_sd_caigsw9_arrow')
    class_a = (By.CSS_SELECTOR, '#nl24')

    # 14.库存分类·二级
    inventory_classification_b = (By.CSS_SELECTOR, '#inpt_custrecord_hq_cgfl110_arrow')
    class_b = (By.CSS_SELECTOR, '#nl36')

    # 15.部门
    # a.下拉
    department_list = (By.CSS_SELECTOR, '#custrecord_hg_department_spu_popup_list')
    # b.选择部门
    department = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    # c.更新
    update = (By.CSS_SELECTOR, '#update')

    # 16.保存
    preservation = (By.CSS_SELECTOR, '#btn_secondarymultibutton_submitter')

    # 17.获取商品编码
    commodity_code = (By.CSS_SELECTOR, '#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div')

