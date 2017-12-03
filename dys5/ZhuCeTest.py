#有了myTestCase以后，再写测试用例就不需要重新写setUp和tearDown方法了
import os

from selenium import webdriver

from dys5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    #三个双引号表示文档字符串，也是一种注释和#号的区别就是这种注释会显示在文档中
    """注册模块测试用例"""
    #因为myTestCase已经实现了setup和tesrDown方法，我们以后再写测试用例就不需要重新实现这两个方法了（setup和tesrDown
    def test_zhu_ce(self):
        """打开注册页面的测试用例"""
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        #driver.current_url #用来获取当前浏览器中的网址
        actual=driver.title #用来获取当前浏览器中的标签页的title
        expected="用户注册 - 道e坊商城 - Powered by Haidao"
        #driver.get_screenshot_as_file截取整个浏览器的图片
        base_path=os.path.dirname(__file__)
        path=base_path.replace('dys5','report/image/')
        #如果报错提示浏览器版本是62--，那么卸载浏览器重新安装

        driver.get_screenshot_as_file(path+"zhuce.png")
        self.assertEqual(actual,expected)

