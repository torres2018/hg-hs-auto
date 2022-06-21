from selenium.webdriver.common.by import By

class ApplicationFormLocator:
    # 客户AR申请单流程
    # ----------------------------------------------------01.客户AR申请单[增加额度]---------------------------------------------------------
    # 01.客户名称
    customer_name = (By.CSS_SELECTOR, '#custrecord_hg_cus_cusname_display')

    # 02.申请类型【信用额度发货】
    application_type = (By.CSS_SELECTOR, '#inpt_custrecord_hg_cus_sqlx3_arrow')
    credit_line_shipment = (By.CSS_SELECTOR, '#nl4')

    # 03.申请金额
    application_amount = (By.CSS_SELECTOR, '#custrecord_hg_cus_changecredit_formattedValue')

    # 04.到期时间
    expiration_time = (By.CSS_SELECTOR, '#custrecord_hg_cus_rq')

    # 05.备注说明【富文本】
    frame_loc = 'cke_custrecord_hg_cus_remarks'  # 切换到目标frame
    remarks = (By.CSS_SELECTOR, '#cke_1_contents > div')

    # 切换到默认页面

    # 06.保存
    preservation = (By.CSS_SELECTOR, '#btn_multibutton_submitter')

    # 07.提交审批
    submit = (By.CSS_SELECTOR, '#custpageworkflow210')

    # 08.审批确认
    approval = (By.CSS_SELECTOR, '#custpageworkflow217')

    # 09.再次审批确认
    confirmation = (By.CSS_SELECTOR, '#custpageworkflow239')

    # 10.标记已冲减
    mark_offset = (By.CSS_SELECTOR, '#custpageworkflow2190')

    # 11.ar申请单单号
    odd_numbers = (By.CSS_SELECTOR, '#main_form > table > tbody > tr:nth-child(1) > td > div.uir-page-title > div.uir-page-title-secondline > div')

    # --------------------------02.已冲减AR申请单[清空额度，审批完成才能重新申请AR---------------------------------------------------
    # 1.事务处理
    transaction_processing = (By.CSS_SELECTOR, '#ns-header-menu-main-item1 > a > span')

    # 2.销售
    sale = (By.XPATH, '//*[@class="ns-menu uir-menu-main ns-menubar"]/li[2]/ul/li[6]')

    # 3.客户AR申请单
    ar_application_form = (By.XPATH, '//*[@class="ns-menu uir-menu-main ns-menubar"]/li[2]/ul/li[6]/ul/li[13]')

    # 4.查看
    see = (By.CSS_SELECTOR, '#row0 > td:nth-child(3) > a.dottedlink.viewitem')

    # 5.确认调整【确认生成一样的效果】
    confirm_adjustment = (By.CSS_SELECTOR, '#custpageworkflow693')

