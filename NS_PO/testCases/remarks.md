**[pytest.ini]**

    1.mark 标记
        markers = TestItemCreation: TestItemCreation for webui
    
    2.模块名的规则，配置测试搜索的模块文件名称
        python_files = test_applicationForm.py
    
    3.类名的规则，配置测试搜索的测试类名
        python_classes = Test*
    
    4.测试用例的路径，可自己配置
        ../pytestproject为上一层的pytestproject文件夹
        ./testcase为pytest.ini当前目录下的同级文件夹
        testpaths = ../testCases
        
    5.方法名的规则，配置测试搜索的测试函数名
        python_functions = test_*
        
    6.日志
        log_cli = True
        
    7.参数配置
        -s：表示输出调试信息，用于显示测试函数中print()打印的信息
        -v：未加前只打印模块名，加v后打印类名、模块名、方法名，显示更详细的信息
        -q：表示只显示整体测试结果
        -vs：这两个参数可以一起使用
        -n：支持多线程或者分布式运行测试用例（需安装：pytest-xdist插件）
        addopts = -s -v
        
 代码
 
        [pytest]
        
        markers =
            TestItemCreation: TestItemCreation for webui
        
        python_files = test_applicationForm.py
        
        python_classes = Test*
        
        testpaths = ../testCases
        
        python_functions = test_*
        
        log_cli = True
        
        addopts = -s -v