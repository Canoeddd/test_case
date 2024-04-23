# -*-coding:utf-8-*-


# 如果有报错信息，把信息打印在file地址下的txt文件中
#file 输出日志的目标文件
#info 需要打印在日志上的信息内容，需要带上实时的时间
import time


def log_error(file,info):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    error_info = current_time+ ' ' + info   #字符串拼接
    #生成一个txt文件
    with open(file, 'a', encoding= 'utf-8') as f:
        f.write(error_info+'\n')