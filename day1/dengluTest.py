import unittest

import time
from selenium import webdriver


class DengLuTest(unittest.TestCase):
    def setUp(self):
        #打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        #浏览器的版本和driver的版本必须匹配才能用窗口最大化
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()


    def test_denglu(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("kkk")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_class_name("login_btn").click()
        #driver.find_element_by_id("password").submit()

