from selenium.webdriver.common.by import By

class SupplierCreationLocator:
    # 创建供应商流程
    # ----------------------------------------------------01.创建供应商---------------------------------------------------------
    # 01.点击【新建供应商】
    new_supplier = (By.CSS_SELECTOR, '#new')

    # ----------------------------------------------------02.供应商详情---------------------------------------------------------
    # 01.公司名称
    corporate_name = (By.CSS_SELECTOR, '#companyname')

    # 02.供应商类别
    # 下拉
    pull_down_a = (By.CSS_SELECTOR, '#inpt_custentity_hg_vend_type2_arrow')
    # 选择供应商类别
    supplier_category = (By.CSS_SELECTOR, '#nl6')

    # 03.品牌
    # a.下拉
    drop_down_a = (By.CSS_SELECTOR, '#parent_actionbuttons_custentity_hq_pinpai1_fs > a:nth-child(2)')
    # b.列表
    list_a = (By.CSS_SELECTOR, '#custentity_hq_pinpai1_popup_list')
    # c.输入品牌
    inp_brand = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_a = (By.CSS_SELECTOR, '#Search')
    # e.选择品牌
    cho_brand = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 04.中文地址
    chinese_address = (By.CSS_SELECTOR, '#custentity_hg_china_address')

    # 05.注册国家
    # a.下拉
    drop_down_b = (By.CSS_SELECTOR, '#parent_actionbuttons_custentity_hg_zhuc_c_country_fs > a:nth-child(2)')
    # b.列表
    list_b = (By.CSS_SELECTOR, '#custentity_hg_zhuc_c_country_popup_list')
    # c.输入注册国家
    inp_country = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_b = (By.CSS_SELECTOR, '#Search')
    # e.选择注册国家
    cho_country = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 06.供货模式
    # 下拉
    pull_down_b = (By.CSS_SELECTOR, '#inpt_custentity_hg_vendor_deli_mode3_arrow')
    # 选择供货模式
    supply_mode = (By.CSS_SELECTOR, '#nl10')

    # 07.货物来源
    # 下拉
    pull_down_c = (By.CSS_SELECTOR, '#inpt_custentity14_arrow')
    # 选择货物来源
    source_of_goods = (By.CSS_SELECTOR, '#nl15')

    # 08.退货地址
    return_address = (By.CSS_SELECTOR, '#custentity_hg_caigou_tuihuo')

    # 09.结算方式
    # 下拉
    pull_down_d = (By.CSS_SELECTOR, '#inpt_terms6_arrow')
    # 选择结算方式
    settlement_method = (By.CSS_SELECTOR, '#nl19')

    # 10.货币
    # a.下拉
    drop_down_c = (By.CSS_SELECTOR, '#custentity_hg_c_dsss_fs > span.uir-field-widget')
    # b.输入货币
    inp_currency = (By.CSS_SELECTOR, '#st')
    # c.点击搜索
    search_c = (By.CSS_SELECTOR, '#Search')
    # d.选择货币
    cho_currency = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')
    # e.更新
    update_c = (By.CSS_SELECTOR, '#update')

    # 11.部门
    # a.下拉
    drop_down_d = (By.CSS_SELECTOR, '#custentity_hg_department_vend_popup_list')
    # b.输入部门
    inp_department = (By.CSS_SELECTOR, '#st')
    # c.点击搜索
    search_d = (By.CSS_SELECTOR, '#Search')
    # d.选择部门
    cho_department = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    # e.更新
    update_d = (By.CSS_SELECTOR, '#update')

    # 12.收件人
    receiver = (By.CSS_SELECTOR, '#custentity_vendor_receiver')

    # 13.城市
    city = (By.CSS_SELECTOR, '#custentity_vendor_city')

    # 14.地址
    location = (By.CSS_SELECTOR, '#custentity_vendor_location')

    # 15.州、省
    province = (By.CSS_SELECTOR, '#custentity_vendor_province')

    # 16.邮编
    zip_code = (By.CSS_SELECTOR, '#custentity_vendor_zipcode')

    # 17.电话
    phone_number = (By.CSS_SELECTOR, '#custentity_vendor_phone_number')

    # 18.收件国家
    # a.下拉
    drop_down_e = (By.CSS_SELECTOR, '#parent_actionbuttons_custentity_vendor_country_fs > a:nth-child(2)')
    # b.列表
    list_e = (By.CSS_SELECTOR, '#custentity_vendor_country_popup_list')
    # c.输入收件国家
    inp_nation = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_e = (By.CSS_SELECTOR, '#Search')
    # e.选择收件国家
    cho_nation = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')

    # 19.统一计量单位
    # a.下拉
    drop_down_f = (By.CSS_SELECTOR, '#parent_actionbuttons_custentity_hg_sol_unite_fs > a:nth-child(2)')
    # b.列表
    list_f = (By.CSS_SELECTOR, '#custentity_hg_sol_unite_popup_list')
    # c.输入统一计量单位
    inp_unit = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_f = (By.CSS_SELECTOR, '#Search')
    # e.选择统一计量单位
    cho_unit = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')

    # 20.采购主体
    """
    # a.下拉
    drop_down_g = (By.CSS_SELECTOR, '#parent_actionbuttons_subsidiary_fs > a:nth-child(2)')
    # b.列表
    list_g = (By.CSS_SELECTOR, '#subsidiary_popup_list')
    # c.输入采购主体
    inp_subject = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_g = (By.CSS_SELECTOR, '#Search')
    # e.选择采购主体
    cho_subject = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')
    """
    inp_subject = (By.CSS_SELECTOR, '#subsidiary_display')

    # 21.返回原default

    # 22.保存
    submitter = (By.CSS_SELECTOR, '#btn_secondarymultibutton_submitter')

    # ----------------------------------------------------03.供应商编号---------------------------------------------------------
    # 23.获取供应商编码
    supplier_code = (By.CSS_SELECTOR, '#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div')
