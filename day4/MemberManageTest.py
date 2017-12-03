import unittest
#1.导入ddt代码库
import ddt
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read

#2.装饰这个类
@ddt.ddt
class MemberMangerTest(unittest.TestCase):
    #3.调用之前写好的read（)方法，获取配置文件中的数据
    member_info=read("member_info.csv")
    # 在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前，只执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)

        cls.driver.quit()

    def test_a_log_in(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        # ActionChains(driver).send_keys(Keys.TAB).send_keys("password") .send_keys(Keys.TAB ).send_keys("1234").send_keys(Keys.ENTER ).perform()
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_name("userverify").submit()
    #python中集合前面的星号表示，表示把集合中的所有元素拆开一个一个写
    #list=["小红"，“小明”]
    #*list="小红"，“小明”
    #星号的作用就是把一个列表拆成两个string
    #假如一个方法需要接收两个参数，那么肯定不能传一个list进去
    #但是如果list中正好也是两个元素，这时在列表前面加一个星号，这时就不认为这时一个列表而是两个参数
    #5.@ddt.data()测试数据来源于read（）方法
    #把数据表中的每一行传入方法，在方法中增加一个参数row

    @ddt.data(*member_info)
    def test_b_add_member(self,row):
        #每组测试数据就是一条测试用例，每条测试用例是独立的
        # 不能因为上一条测试用例执行失败导致下一组数据不能被正常执行，所以这里不推荐用for循环
        #应该用ddt装饰器去修饰这个方法，达到每条测试用例独立执行的目的
        #ddt是数据驱动测试 data driver test   将ddt解压到：C:\Users\51Testing\AppData\Local\Programs\Python\Python35\Lib\site-packages
        #4.注释掉for循环，改变代码的缩进，使方法中的代码比方法声明缩进四个空格，快捷键shift+tab
       # for row in read("member_info.csv"):
           # print("添加会员")
        driver = self.driver

        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        # 如果frame没有name属性时，我们可以通过其他方式定位iframe标签，把定位好的页面元素传给driver.switch_to.frame(iframe_html )方法也可以
        iframe_css = "#mainFrame"
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        #
        #
        #driver.find_element_by_css_selector('value="'+row[2]+'"').click()
        driver.find_element_by_css_selector('[value="{0}"]'.format(row[2])).click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()

        #z之前的代码是能够自动运行，但是还不能自动判断程序运行的是否正确
        #自动化代码不能找人一直总是盯着运行，检查是否执行正确
        #actual s实际结果，执行测试用例后，页面是实际显示的结果
        actual=driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        #expected 期望结果，来自手动测试用例或者需求文档，配置文件
        expected=row[0]
        #断言类似于if else语句，是用来做判断的
       # if actual == expected :
           # print("测试通过")
        #else:
          #  print("测试失败")
        #断言叫assert,断言是框架提供的，要想调用断言，那么必须加self. 因为我们的测试用例类继承了框架中的TestCase类，也继承了这个类中的断言
        #所以我们可以直接用断言方法
        #断言有几个特点
        #1.断言比较简洁
        #2.断言关注于错误的测试用例，只有断言出错的时候才会打印信息，正确没有任何信息提示
        #3.断言报错时，后面的代码将不会继续执行，前面的步骤失败，后面的步骤就不需要继续尝试，浪费性能





        # 切换到父框架
        # driver.switch_to.parent_frame()
        # 切换到网页的根节点
        driver.switch_to.default_content()
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()



