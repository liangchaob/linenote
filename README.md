# linenote 1.0
linenote是一个简单地单行日记应用，旨在能在CLI界面下快速记录与回顾日志

# 运行与使用
该脚本基于python2.7

    python linenote.py
    
运行之后会在linenote.py当前所在目录下建立一个名叫linenote.csv的档案文件，并要求用户输入日志内容

    2015-10-20 17:09:34 : 这是一行linenote日志

再次运行linenote.py会显示历史日志，并请求输入新的日志

    "2015-10-20 17:09:34","这是linenote日志"

    2015-10-20 17:12:13 : 这是又一行linenote日志
日志文件可以使用Excel打开与处理

# 配置
可以使用编辑器打开linenote.py文件修改filename调整档案文件名（默认为linenote.csv）

    # 配置档案文件名
    fileName = 'linenote.csv'
