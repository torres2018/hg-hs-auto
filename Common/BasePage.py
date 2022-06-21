# Author:lilianjun
# -*- coding:utf-8 -*-
"""
1.生成执行日志;测试用例的执行日志
2.测试用例的任何一行代码失败,都希望能在日志当中看到异常信息,并且生成失败的网页截图
3.精简一下我的 pageobjects 页面
测试用例 = 页面对象(步骤+断言) + 测试数据
页面对象 = 页面行为 + 页面元素定位
页面行为 = selenium webdrive基本 API{查找元素\等待\点击\输入\清除\文本获取\属性获取}组合起来的
对 WebDrive 的基础函数封装一下.加入日志\异常处理\失败截图
BasePage 具备以上三点
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging, time
from selenium.webdriver.common.action_chains import ActionChains
from Common import file_path
from Common.Logger import MyLogger

MyLog = MyLogger(logger='TestMyLog').getlog()

class basePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, loc, timeout=20, poll_frequency=0.5, model=None):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:None
        """
        logging.info('{} 等待元素可见:{}'.format(model, loc))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
            '''visibility_of_element_located判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
            # WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
            '''presence_of_element_located判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
            '''presence_of_element_located的校验程度轻一些，在页面跳转之后判断某种标志是否出现用这个快一些；特殊情况下校验无边框的元素也会用到这个'''
            end = time.time()
            MyLog.info('等待时长:%.2f 秒' % (end - start))
        except:
            MyLog.exception('{} 等待元素可见失败:{}'.format(model, loc))
            # 截图
            self.save_webImgs(model)
            raise

    # 等待元素不可见
    def wait_eleNoVisible(self, loc, timeout=20, poll_frequency=0.5, model=None):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:None
        """
        logging.info('{} 等待元素不可见:{}'.format(model, loc))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until_not(EC.visibility_of_element_located(loc))
            end = time.time()
            MyLog.info('等待时长:%.2f 秒' % (end - start))
        except:
            MyLog.exception('{} 等待元素不可见失败:{}'.format(model, loc))
            # 截图
            self.save_webImgs(model)
            raise

    # 查找一个元素element
    def find_Element(self, loc, model=None):
        MyLog.info('{} 查找元素 {}'.format(model, loc))
        try:
            return self.driver.find_element(*loc)
        except:
            MyLog.exception('查找元素失败.')
            # 截图
            self.save_webImgs(model)
            raise

    # 查找元素elements
    def find_Elements(self, loc, model=None):
        MyLog.info('{} 查找元素 {}'.format(model, loc))
        try:
            return self.driver.find_element(*loc)
        except:
            MyLog.exception('查找元素失败.')
            # 截图
            self.save_webImgs(model)
            raise

    # 输入操作
    def input_Text(self, loc, text, model=None):
        # 查找元素
        ele = self.find_Element(loc, model)
        # 输入操作
        MyLog.info('{} 在元素 {} 中输入文本: {}'.format(model, loc, text))
        try:
            ele.send_keys(text)
        except:
            MyLog.exception('输入操作失败')
            # 截图
            self.save_webImgs(model)
            raise

    # 清除操作
    def clean_Input_Text(self, loc, model=None):
        ele = self.find_Element(loc, model)
        # 清除操作
        MyLog.info('{} 在元素 {} 中清除'.format(model, loc))
        try:
            ele.clear()
        except:
            MyLog.exception('清除操作失败')
            # 截图
            self.save_webImgs(model)
            raise

    # 点击操作
    def click_Element(self, loc, model=None):
        # 先查找元素在点击
        ele = self.find_Element(loc, model)
        # 点击操作
        MyLog.info('{} 在元素 {} 中点击'.format(model, loc))
        try:
            ele.click()
        except:
            MyLog.exception('点击操作失败')
            # 截图
            self.save_webImgs(model)
            raise

    # 鼠标悬停
    """
        ActionChains 类提供了鼠标操作的常用方法：           
        perform()： 执行所有 ActionChains 中存储的行为；            
        context_click()： 右击；            
        double_click()： 双击；            
        drag_and_drop(source, target)： 拖动；           
        move_to_element()： 鼠标悬停
    """
    def move_to_action(self, loc, model=None):
        # 先查找元素再悬停
        ele = self.find_Element(loc, model)
        # 点击操作
        MyLog.info('{} 在元素 {} 上悬停'.format(model, loc))
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            MyLog.exception('鼠标悬停失败')
            # 截图
            self.save_webImgs(model)
            raise

    # 获取文本内容
    def get_Text(self, loc, model=None):
        # 先查找元素在获取文本内容
        ele = self.find_Element(loc, model)
        # 获取文本
        MyLog.info('{} 在元素 {} 中获取文本'.format(model, loc))
        try:
            text = ele.get_attribute('textContent')
            MyLog.info('{} 元素 {} 的文本内容为 {}'.format(model, loc, text))
            return text
        except:
            MyLog.exception('获取元素 {} 的文本内容失败,报错信息如下:'.format(loc))
            # 截图
            self.save_webImgs(model)
            raise

    # 获取属性值
    def get_Element_Attribute(self, loc, model=None):
        # 先查找元素在去获取属性值
        ele = self.find_Element(loc, model)
        # 获取元素属性值
        MyLog.info('{} 在元素 {} 中获取属性值'.format(model, loc))
        try:
            ele_attribute = ele.get_attribute()
            MyLog.info('{} 元素 {} 的文本内容为 {}'.format(model, loc, ele_attribute))
            return ele_attribute
        except:
            MyLog.exception('获取元素 {} 的属性值失败,报错信息如下:'.format(loc))
            self.save_webImgs(model)
            raise

    # iframe 切换
    def switch_iframe(self, frame_refer, timeout=20, poll_frequency=0.5, model=None):
        # 等待 iframe 存在
        MyLog.info('iframe 切换操作:')
        try:
            # 切换 == index\name\id\WebElement
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(frame_refer))
            time.sleep(3)
            MyLog.info('切换成功')
        except:
            MyLog.exception('iframe 切换失败!!!')
            # 截图
            self.save_webImgs(model)
            raise

    # 弹框确认
    def switch_alert(self, model=None):
        # 等待 弹出框 存在
        MyLog.info('弹窗确认操作:')
        try:
            # WebDriverWait(self.driver, timeout, poll_frequency).until(EC.alert_is_present)
            alert_object = self.driver.switch_to.alert
            alert_object.accept()
            time.sleep(3)
            MyLog.info('弹框确认成功')
        except:
            MyLog.exception('弹框确认失败!!!')
            # 截图
            self.save_webImgs(model)
            raise

    # 窗口切换 = 如果是切换到新窗口,new. 如果是回到默认的窗口,default
    def switch_window(self, name, model=None):
        """
        调用之前要获取window_handles
        :param name: new 代表最新打开的一个窗口. default 代表第一个窗口. 其他的值表示为窗口的 handles
        :param cur_handles:
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:
        """
        try:
            if name == 'new':
                MyLog.info('切换到最新打开的窗口')
                all_handles = self.driver.window_handles
                self.driver.switch_to.window(all_handles[-1])  # 提示的方法并一定正确，这里提示的swich_to
                time.sleep(3)
            elif name == 'default':
                MyLog.info('切换到默认页面')
                self.driver.switch_to.default_content()
                time.sleep(3)
            else:
                MyLog.info('切换到为 handles 的窗口')
                self.driver.swich_to.window(name)

        except:
            MyLog.exception('切换窗口失败!!!')
            # 截图
            self.save_webImgs(model)
            raise

    """
    def switch_handle(self):
        handles = self.driver.window_handles
        for newhandle in handles:
            if newhandle != self.driver.current_window_handle:
                self.driver.switch_to.window(newhandle)
    """
    # 截图
    def save_webImgs(self, model=None):
        # filepath = 指图片保存目录/model(页面功能名称)_当前时间到秒.png[F:\HS\UI测试-NS\NS_PO\TestNS\Imgs]
        file_path = 'F:\\HS\\UI测试-NS\\NS_PO\\TestNS\\Imgs'
        # 当前时间
        # dateNow = str(date.today()) + '-' + str(int(time.time()))
        dateNow = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 路径
        filePath = '{}\\{}_{}.png'.format(file_path, model, dateNow)
        try:
            self.driver.save_screenshot(filePath)
            MyLog.info('截屏成功,图片路径为{}'.format(filePath))
        except:
            MyLog.exception('截屏失败!')

    # 判断元素是否存在
    def is_element_exist(self,loc):
        try:
            self.driver.find_element(*loc)
            return True
        except:
            return False

    def write_data(self, path, code):
        try:
            # 1.写出文件 w:文件不存在创建，在写入，存在：清空内容再写入，a：文件不存在创建，再写入，存在：追加
            w_path = path
            f = open(w_path, "w", encoding="utf-8")
            # 2.准备数据
            data = str(code)
            # 3.写出文件
            f.write(data)
            # 4.关闭流
            f.close()
            MyLog.info('数据写入成功')
        except:
            MyLog.exception('数据写入失败!!!')
            raise

    def read_data(self, path):
        try:
            # 1.打开文件，读取数据
            r_path = path
            src = open(r_path, "r", encoding="utf-8")
            # 2.读取文件
            data = src.read()
            MyLog.info('数据读取成功')
            # 3.分析处理
            return data
        except:
            MyLog.exception('数据读取失败!!!')
            raise

"""
    隐式等待和显示等待都存在时，超时时间取二者中较大的'''
    locator = (By.ID,'kw')
    driver.get(base_url)
     
    WebDriverWait(driver,10).until(EC.title_is(u"百度一下，你就知道"))
    '''判断title,返回布尔值'''
     
    WebDriverWait(driver,10).until(EC.title_contains(u"百度一下"))
    '''判断title，返回布尔值'''
     
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
    '''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
     
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'su')))
    '''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
     
    WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(by=By.ID,value='kw')))
    '''判断元素是否可见，如果可见就返回这个元素'''
     
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.mnav')))
    '''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''
     
    WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.mnav')))
    '''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''
     
    WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='u1']/a[8]"),u'设置'))
    '''判断指定的元素中是否包含了预期的字符串，返回布尔值'''
     
    WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'#su'),u'百度一下'))
    '''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''
     
    #WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
    '''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
    #注意这里并没有一个frame可以切换进去
     
    WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#swfEveryCookieWrap')))
    '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
    #注意#swfEveryCookieWrap在此页面中是一个隐藏的元素
     
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='u1']/a[8]"))).click()
    '''判断某个元素中是否可见并且是enable的，代表可点击'''
    driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wrapper']/div[6]/a[1]"))).click()
     
    #WebDriverWait(driver,10).until(EC.staleness_of(driver.find_element(By.ID,'su')))
    '''等待某个元素从dom树中移除'''
    #这里没有找到合适的例子
     
    WebDriverWait(driver,10).until(EC.element_to_be_selected(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]")))
    '''判断某个元素是否被选中了,一般用在下拉列表'''
     
    WebDriverWait(driver,10).until(EC.element_selection_state_to_be(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]"),True))
    '''判断某个元素的选中状态是否符合预期'''
     
    WebDriverWait(driver,10).until(EC.element_located_selection_state_to_be((By.XPATH,"//*[@id='nr']/option[1]"),True))
    '''判断某个元素的选中状态是否符合预期'''
    driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()
     
    instance = WebDriverWait(driver,10).until(EC.alert_is_present())
    '''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
    print instance.text
    instance.accept()
     
    driver.close()
    注意：WebDriver.implicitly_wait() 只能设置查找元素和执行命令的超时，对页面加载操作的超时无效。
    注意：selenium 默认的页面加载超时为 300 秒。
    selenium 中所有超时方法的参数单位都为秒。内部为将参数乘1000 转成毫秒。
    WebDriver.implicitly_wait() 设置的超时并不适用于用户操作导致的页面重新加载或页面脚本对 DOM 整体结构的改变，遇到这两种情况考虑适用其他等待条件。
"""