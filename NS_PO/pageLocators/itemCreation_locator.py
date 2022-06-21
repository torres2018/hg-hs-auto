from selenium.webdriver.common.by import By

class ItemCreationLocator:
    # 货品创建流程
    # ----------------------------------------------------一.货品创建---------------------------------------------------------
    # 01.引用商品
    # a.下拉
    drop_down_a = (By.CSS_SELECTOR, '#parent_actionbuttons_custitem_hq_sku_spu_v_fs > a:nth-child(2)')
    # b.列表
    list_a = (By.CSS_SELECTOR, '#custitem_hq_sku_spu_v_popup_list')
    # c.输入商品
    inp_product = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_a = (By.CSS_SELECTOR, '#Search')
    # e.选择商品
    cho_product = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 02.规格1[同一商品下不能有规格相同的货品]
    # a.下拉
    drop_down_b = (By.CSS_SELECTOR, '#parent_actionbuttons_custitem_hq_sku_spu_spec_1_value_fs > a:nth-child(2)')
    # b.列表
    list_b = (By.CSS_SELECTOR, '#custitem_hq_sku_spu_spec_1_value_popup_list')
    # c.输入规格1
    inp_norms = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_b = (By.CSS_SELECTOR, '#Search')
    # e.选择规格1
    cho_norms = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 03.规格2
    # a.下拉
    drop_down_c = (By.CSS_SELECTOR, '#parent_actionbuttons_custitem_hq_sku_spu_2_value_fs > a:nth-child(2)')
    # b.列表
    list_c = (By.CSS_SELECTOR, '#custitem_hq_sku_spu_2_value_popup_list')
    # c.输入规格2
    inp_specs = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_c = (By.CSS_SELECTOR, '#Search')
    # e.选择规格2
    cho_specs = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 04.保存
    preservation = (By.CSS_SELECTOR, '#btn_secondarymultibutton_submitter')

    # 05.获取货品编码
    item_code = (By.CSS_SELECTOR, '#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div')
