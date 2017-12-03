#要读csv文件，首先要准备一个csv文件
#1.导入csv的包
#csc是python语言内置的包，比较常用，开发和测试所有项目都有可能用到
import csv
#2.要想读取文件的信息，首先要知道文件的存放路径
#字符串前面加一个字符r，表示反斜杠是普通字符，不看做转义字符
path=r"C:\Users\51Testing\PycharmProjects\untitled2\data\member_info.csv"
#3.要想读文件的内容，首先要通过路径打开文件
file=open(path,'r')
#4.通过csv代码库，读取csv格式的内容
data_table=csv.reader(file)
#5.遍历data_table，分别打印每一行数据
for row in data_table:
    print(row)