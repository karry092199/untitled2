import unittest


if __name__ == '__main__':
    #defaultTestLoader 默认的测试用例加载器，用于寻找符合一定规则的测试用例
    #discover 发现
    suite = unittest.defaultTestLoader.discover( './dys5', pattern='*Test.py')
    #执行suite中的所有的测试用例
    #TextTestRunner  文本测试用例运行器
    #TextTestRunner 首字母大写，说明他是一个类，类不能直接调用方法，必须要实例化对象才能调用方法
    #python中实例化不需要new关键字，直接在类后面加一对小括号即可
    unittest.TextTestRunner().run(suite)
