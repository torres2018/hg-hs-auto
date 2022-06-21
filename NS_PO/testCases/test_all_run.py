# coding=utf-8
import pytest
import os
"""
一.调用登录作为前置条件：
    具体方法：（三种）
    1.函数或类方法直接传fixture的函数参数名
    2.使用装饰器@pytest.mark.usefixtures()
    3.设置autouse=True自动使用
    
二.allure报告的方法：
    @allure.feature # 用于定义被测试的功能，被测产品的需求点
    @allure.story # 用于定义被测功能的用户场景，即子功能点
    with allure.step # 用于将一个测试用例，分成几个步骤在报告中输出
    allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
    @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
"""
if __name__ == '__main__':
    try:
        for one in os.listdir('../report/tmp'):  # one 是每一个文件名
            if '.json' in one or '.txt' in one:  # 以后有环境配置文件在里面，所以做了判定！
                os.remove(f'../report/tmp/{one}')
    except:
        print('第一次运行pytest.main()')

    pytest.main(['-s', '--alluredir', '../report/tmp'])  # 执行所有测试用例，并生成报告
    # pytest.main(['test_deliveryNotice.py', '-s', '--alluredir', '../report/tmp'])  # 执行指定测试用例，并生成报告

    os.system('allure generate ../report/tmp -o ../report/report --clean')  # 转化成可视化allure报告
    """
    allure工作流程
        1- 生成报告需要的源数据：pytest运行测试用例  pytest.main()----一定有结果（后面的报告的数据来源）
        2- 有了源数据----一个工具去读取转化源数据得到  allure -----可视化报告 
    """
