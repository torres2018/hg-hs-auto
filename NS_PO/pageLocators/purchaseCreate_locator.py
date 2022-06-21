from selenium.webdriver.common.by import By

class PurchaseCreateLocator:
    # 采购单创建流程
    # ----------------------------------------------------01.库存列表---------------------------------------------------------
    # 1.输入货品编码
    inp_code = (By.XPATH, '//*[@id="itemid"]')

    # 2.点击搜索
    click_search =(By.XPATH, '//*[@id="search"]')

    # 3.添加进入购物车
    add_to_cart = (By.XPATH, '//*[@id="info_listrow0"]/td[2]/a')

    # ----------------------------------------------------02.选择PO类型-------------------------------------------------------
    # 1.跳转到新窗口

    # 2.点击下拉
    drop_down_a = (By.CSS_SELECTOR, '#inpt_po_or_to1_arrow')

    # 3.选择PO类型
    po_type = (By.CSS_SELECTOR, '#nl2')

    # ----------------------------------------------------03.购物车详情-------------------------------------------------------
    # 进入添加购物车界面
    # 01.选择仓库
    drop_down_b = (By.CSS_SELECTOR, '#inpt_location3_arrow')
    wareHouse = (By.XPATH, '//*[@id="nl51"]')

    # 02.采购数量
    purchase_quantity = (By.XPATH, '//*[@id="quantity_formattedValue"]')

    # 03.结算方式
    drop_down_c = (By.XPATH, '//*[@id="inpt_settlement_method5_arrow"]')
    settlementMethod = (By.XPATH, '//*[@id="nl74"]')

    # 04.供货模式
    drop_down_d = (By.XPATH, '//*[@id="inpt_supply_mode6_arrow"]')
    deliveryOfGoods = (By.XPATH, '//*[@id="nl91"]')

    # 05.添加至PO购物车
    submit = (By.XPATH, '//*[@id="submitter"]')

    # 06.弹框确认

    # 07.点击提交，进入购物车列表
    preservation = (By.XPATH, '//*[@id="ext-element-4"]/div/button[1]')

    # ----------------------------------------------------04.PO购物车列表-------------------------------------------------------
    # 批量生成PO单
    # 1.输入货品编码
    inp_code_a = (By.CSS_SELECTOR, '#sub_itemid')

    # 2.点击搜索
    search = (By.CSS_SELECTOR, '#search')

    # 3.勾选单据
    checkImg = (By.CSS_SELECTOR, '#checkbox1_fs > img')

    # 5.生成PO单
    generatePo = (By.CSS_SELECTOR, '#submitter')

    # ----------------------------------------------------05.刷新获取采购单号-------------------------------------------------------
    # 1.点击刷新
    refresh = (By.XPATH, '//*[@id="refresh"]')

    # ----------------------------------------------------06.点击单号链接-------------------------------------------------------
    # 1.点击采购单链接，进入采购单
    poLink = (By.XPATH, '//*[@id="poidlink"]')

    # ----------------------------------------------------07.PO编辑-------------------------------------------------------
    # 1.编辑采购单
    edit = (By.CSS_SELECTOR, '#edit')

    # 2.是否计算税收
    drop_down_e = (By.CSS_SELECTOR, '#inpt_custbody_hg_if_compute_s2')
    noTax = (By.CSS_SELECTOR, '#nl4')

    # 3.交付日期
    deliveryDate = (By.CSS_SELECTOR, '#custbody_hg_jiaof_fdate')

    # 4.保存
    preservePo = (By.CSS_SELECTOR, '#btn_secondarymultibutton_submitter')

    # ----------------------------------------------------08.PO单审核-------------------------------------------------------
    # 08.审批确认
    adopt = (By.CSS_SELECTOR, '#custpage_purchase_order')

    # 08.审批通过
    access = (By.CSS_SELECTOR, '#custpageworkflow398')

