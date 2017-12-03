import unittest

import time
from select import select

from selenium  import webdriver
from selenium.webdriver.support.select import Select


class MemberMangTest(unittest.TestCase):
    #变量前面加上self，表示这个变量是类的属性，可以被所有的方法访问
    def setUp(self):
       #打开浏览器
       #driver声明在setUp方法之内，不能被其他方法访问
        self.driver= webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        #quit()退出浏览器
        #close()关闭一个浏览器
        #代码编写和调试的时候需要在quit方法前加一个时间等待，方便看清楚执行过程
        #正式运行的时候去掉时间等待，为了提高程序执行速度
        time.sleep(20)
        #self.driver.quit()

    def test_add_member(self):
        driver=self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_name("userverify").submit()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("凯凯test")
        driver.find_element_by_name("mobile_phone").send_keys("13716179634")
        br=driver.find_element_by_name("sex")
        Select(br).select_by_index(0)
        driver.find_element_by_id("birthday").send_keys("1999-09-21")











