import unittest

import time

from day6.data_base.connerctDB import connDb
from dys5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("kaili")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("userpassword2").send_keys("123456")
        driver.find_element_by_name("mobile_phone").send_keys("13716179921")
        driver.find_element_by_name("email").send_keys("123499@qq.com")
        driver.find_element_by_class_name("reg_btn").click()

        #检查数据库中新增的记录的用户名和我们输入的用户名是否一致
        expected="kaili"
        time.sleep(3)
        actual=connDb()[1]
        self.assertEqual(expected,actual)
        print(connDb()[1])

