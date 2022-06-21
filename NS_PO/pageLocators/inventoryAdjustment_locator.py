from selenium.webdriver.common.by import By

class InventoryAdjustmentLocator:
    # 库存调整单流程
    # ----------------------------------------------------01.库存调整---------------------------------------------------------
    # 1.附属公司
    # a.下拉
    drop_down_a = (By.CSS_SELECTOR, '#parent_actionbuttons_subsidiary_fs > a:nth-child(2)')
    # b.列表
    list_a = (By.CSS_SELECTOR, '#subsidiary_popup_list')
    # c.输入子公司
    inp_company = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_a = (By.CSS_SELECTOR, '#Search')
    # e.选择子公司
    cho_company = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')

    # 2.调整科目
    # a.下拉
    drop_down_b = (By.CSS_SELECTOR, '#parent_actionbuttons_account_fs > a:nth-child(2)')
    # b.列表
    list_b = (By.CSS_SELECTOR, '#account_popup_list')
    # c.选择
    cho_course = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')

    # 3.货品【PN0000000057161】
    # a.下拉
    drop_down_c = (By.CSS_SELECTOR, '#parent_actionbuttons_inventory_item_fs > a:nth-child(2)')
    # b.列表
    list_c = (By.CSS_SELECTOR, '#item_popup_list')
    # c.输入【PN0000000057161】
    inp_product = (By.CSS_SELECTOR, '#st')
    # d.点击搜索
    search_c = (By.CSS_SELECTOR, '#Search')
    # e.选择货品
    cho_product = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr:nth-child(2) > td:nth-child(2) > a')

    # 4.地点[深圳仓-新香港公司]
    # 点击一下
    click_one = (By.CSS_SELECTOR, '#inventory_splits > tbody > tr.uir-machine-row.uir-machine-row-odd.listtextnonedit.uir-machine-row-focused > td:nth-child(3) > div')
    # a.下拉
    drop_down_d = (By.CSS_SELECTOR, '#parent_actionbuttons_inventory_location_fs > a:nth-child(2)')
    # b.列表
    list_d = (By.CSS_SELECTOR, '#location_popup_list')
    # c.输入【深圳仓-新香港公司】
    inp_warehouse = (By.CSS_SELECTOR, '#st')
    # d.搜索
    search_d = (By.CSS_SELECTOR, '#Search')
    # e.选择该仓库
    cho_warehouse = (By.CSS_SELECTOR, '#inner_popup_div > table > tbody > tr > td:nth-child(2) > a')

    # 5.调整数量
    # 点击一下
    click_two = (By.CSS_SELECTOR, '#inventory_splits > tbody > tr.uir-machine-row.uir-machine-row-odd.listtextnonedit.uir-machine-row-focused > td:nth-child(7) > div')
    # a.调整数量
    inp_quantity = (By.CSS_SELECTOR, '#adjustqtyby_formattedValue')

    # 6.添加
    add_to = (By.CSS_SELECTOR, '#inventory_addedit')

    # 7.保存
    preservation = (By.CSS_SELECTOR, '#secondarysubmitter')

    # 8.库存调整单号
    odd_numbers = (By.CSS_SELECTOR, '#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div')

