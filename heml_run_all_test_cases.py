import os
import smtplib
import unittest
#HEMLTestRunner 是基于unittest框架的一个扩展，可以自己在网上自行下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f=open(path,'rb')
    mail_body=f.read()  #读取html报告的内容，作为邮件的正文
    f.close()

    #要想发邮件，我们要把二进制的内容转成MIME格式
    #MIME multipurse多用途 internet 互联网 Mail 邮件 Extension 扩展
    #MIME 这种格式是对邮件协议的一个扩展，使邮件不仅支持文本，还支持多种格式
    #比如：图片，音频、二进制文件等
    msg = MIMEText(mail_body,'html','utf-8')
    #上面是邮件的正文，但是对于一个邮件来讲，除了正文，还需要主题，发件人、收件人
    #msg是字典的类型，字典类似于数组，区别是：1.字典是无序的

    msg['Subject']=Header("自动化测试报告",'utf-8')
    #如果想用客户端软件或者自己写代码登录邮箱，很多类型的邮箱需要单独设置一个客户端授权码
    #授权码，为了邮箱安全着想
    msg['From']='bwftest126@126.com'
    msg['To']='wumi0425@163.com'

    #现在邮件内容已经准备好了，下面开始发送邮件
    #发送邮件的手动步骤：
    #1.打开登录页面，即连接邮箱服务器
    #要想链接服务器，首先必须搞清楚网络传输协议
    #http,https.ftp,socket
    #发邮件的协议，一般有三种，你要查看你的邮箱是那种协议
    #126邮箱支持这三种协议pop3,smtp,imap
    #我们要选择一种传输协议，用来发邮件，smtp
    #smtp simple  mail  transful protocol简单邮件传输协议
    #首选导入smtplib的代码库
    smtp = smtplib.SMTP()  #实例化一个SMTP类的对象
    smtp.connect("smtp.126.com")  #连接126邮箱的服务器地址


    #2.登录邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
    #3.发送邮件
    #注意msg是MIME类型，需要转成String类型再发送
    smtp.sendmail('bwftest126@126.com', 'wumi0425@163.com', msg.as_string())
    #4.退出邮箱
    smtp.quit()
    print('email has sent out!')


if __name__ == '__main__':
    #str 是String  f 是format格式
    #strftim（）通过这个方法可以定义时间的格式
    #Y year年 m month月  d day日  H hour 小时  M minute 分 S second秒
    now=time.strftime("%Y-%m-%d_%H-%M-%S")
    suite=unittest.defaultTestLoader.discover('./dys5','*Test.py')
   # unittest.TextTestRunner(suite) 文本测试运行器
    #现在用html的测试用例运行器
    #html的测试用例运行器最终会生成一个heml格式的测试报告

    #我们是不是至少找制定测试报告的路径
    base_path=os.path.dirname(__file__)
    path=base_path+"/report/report"+now+".html"
    file=open(path,'wb')
    HTMLTestRunner(stream=file, title="海盗商城测试报告", description="测试环境：windows server2008+Chrome").run(suite)
    file.close()
    #我们要把html报告作为邮件正文，发送邮件
    send_mail(path)
    #这时生成的测试报告，只显示类名和方法名，只能给专业的人士看
    #我们应该把相关的手动测试用例的标题加到我们的测试报告中
    #我们自动化测试用例是从手工测试用例中挑出来的，手工测试用例怎么写我们就怎么编译代码
    #所以我们的代码里面应该可以体现手动测试用例的标题
    #新的测试报告会覆盖原来的测试报告，如果想把所有测试报告都保存起来怎么做
    #加一个时间戳，按照当前时间计算一个数字，把数字作为文件名的一部分，避免了文件名重复的问题
    #现在我们的html格式的测试报告生成了，当测试用例全部执行完成我们应该生成一封提醒邮件，通知所有
    #关心测试结果的人
