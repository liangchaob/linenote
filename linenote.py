# -*- coding: UTF-8 -*-
# 引入os模块
import os

# 引入datatime模块
import time

# 引入sys模块，并将默认字符格式转为utf-8
import sys
sys.path.append("./")
reload(sys)
sys.setdefaultencoding( "utf-8" )


# 配置档案文件名
fileName = 'linenote.csv'

# 获取当前时间与调整格式
timeNow = time.strftime("%Y-%m-%d %H:%M:%S")


# 主函数
def main():
    # 判断档案文件是否存在，不存在则新建
    if os.path.exists(fileName) == False:
        noteFile=open(fileName,'w')
        noteFile.close()
    # 如果文件存在则先显示历史内容
    else:
        printNote()
    # 输入一行日记
    content = str(raw_input(timeNow+" : "))
    # 写入文件
    writeNote(content)


# 遍历文件内容
def printNote():
    noteFile = open(fileName,'r')
    for line in noteFile:
        print(line)
    noteFile.close()


# 写入文件内容
def writeNote(content):
    noteFile = open(fileName,'a')
    # 配置行文件写入格式
    lineInsert = "\""+timeNow + "\",\"" + content+'\"\n'
    noteFile.writelines([lineInsert])
    noteFile.close()


# 运行主函数
if __name__ == '__main__':
    main()
