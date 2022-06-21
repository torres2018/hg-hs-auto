from selenium.webdriver.common.by import By

class DeliveryNoticeLocator:
    # ----------------------------------------------------01.送货通知----------------------------------------------------
    #1.输入采购单号
    goods_input = (By.CSS_SELECTOR, '#search_po_number')

    #2.搜索
    search = (By.CSS_SELECTOR, '#search')

    #3.输入今天日期
    today = (By.CSS_SELECTOR, '#send_time')

    #4.输入发货数量
    quantity = (By.CSS_SELECTOR, '#custpage_sendquantity1_formattedValue')

    #5.点击提交
    submit = (By.CSS_SELECTOR, '#submitter')

    #6.点击刷新
    refresh = (By.CSS_SELECTOR, '#custpage_refresh')

    #7.打印HS交货单号get_attribute('textContent')
    oddtext = (By.CSS_SELECTOR, '#info_listrow0 > td:nth-child(6)')
