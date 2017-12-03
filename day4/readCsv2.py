#1.之前的readcsv不能被其他测试用例调用，所以应该给这段代码封装到一个方法里面
#2.每个测试用例的路径不同，所以path应该作为参数传入到这个方法中
#3.我们打开了一个文件但是并没有关闭，最终可能会造成内存泄露
import csv
import os


def read(file_name):
    #所有的重复代码的出现都是程序设计的不合理
    #重复的代码应该封装到一个方法里面
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/"+file_name)
    #file=open(path,'r')
    #with语句是一个代码块，代码块中的内容都要缩进4个空格
    #with代码块可以自动关闭with中声明的变量
    #try ...finally.... 也可以保证程序中间发生异常时,文件最后也可以关闭
    #  但是finally语法的可读性比较差,写起来比较容易出错, 一般都用with语句代替finally
    #因为file文件一旦被关闭，里面的数据也随着消失
    # 所以单独声明一个列表叫result来保存里面的数据


    result=[]
    with open(path,'r') as file:
        data_table=csv.reader(file)
        for row in data_table:
            result.append(row)
            #print(row)

    return result
        #如果在打开和关闭程序的代码中间发生了异常，导致后面的代码不能正常运行
        #file.close()也不执行了，这时文件仍不能关闭
        #file.close()
        #应该用with语句实现文件的关闭
if __name__ == '__main__':
    #path = r"C:\Users\51Testing\PycharmProjects\untitled2\data\member_info.csv"
    #4.这个路径是一个绝对路径，我们工作中一个项目不止一个人编写代码，没法统一要求大家都把项目代码放在一个路径下
    #这个文件因为在项目中，他的路径也会随着项目变化
    #所以应该在代码中,t通过当前代码文件的路径，根据相对位置，找到csv文件
    #首先要找到当前文件路径

    #os  是操作系统,path是路径，dir是directory目录，__file__是python内置的变量，指的是当前文件
    #current_file_path=os.path.dirname(__file__)
    #print(current_file_path )
    #我们真正想要的路径csv文件路径
    #path=current_file_path.replace("day4","data/member_info.csv")
    #print(path)
    member_info=read("member_info.csv")
    #print(member_info )
    for row in member_info :
        print(row)
        #print(row[0]) 打印姓名




    #5.读出数据不是目的，目的是通过数据驱动测试，所以应该把数据作为方法的返回值方便进一步调用它




