# - * - coding: utf-8 - * -
import os
#重写JD_Spider.py文件
os.chdir('F:\\Program_Stores\\Python\\2016-04-26\\SpiderModel\\JDSpider\\JDSpider\\spiders')       # 跳到目标路径
if not os.path.exists('JD_Spider.py'): # 看一下这个文件是否存在
    exit(-1)                       #不存在就退出
lines = open('JD_Spider.py').readlines()  #打开文件，读入每一行
JD_Spider = open('F:\\Program_Stores\\Python\\2016-04-26\\Auto\\JDSpider\\JDSpider\\spiders\\JD_Spider.py','w')  #打开需要写入的脚本
for s in lines:
    # replace是替换，write是写入
    JD_Spider.write(s.replace('$$query$$','咖啡'))    
JD_Spider.close()  # 关闭文件


#重写settings.py文件
os.chdir('F:\\Program_Stores\\Python\\2016-04-26\\SpiderModel\\JDSpider\\JDSpider')       # 跳到目标路径
if not os.path.exists('settings.py'): # 看一下这个文件是否存在
    exit(-1)                       #不存在就退出
lines_s = open('settings.py').readlines()  #打开文件，读入每一行
settings = open('F:\\Program_Stores\\Python\\2016-04-26\\Auto\\JDSpider\\JDSpider\\settings.py','w')  #打开需要写入的脚本
for a in lines_s:
    # replace是替换，write是写入
    settings.write(a.replace('$$query$$','咖啡'))    
settings.close()  # 关闭文件

#重写JD_Spider.py文件
os.chdir('F:\\Program_Stores\\Python\\2016-04-26\\SpiderModel\\JDSpider\\JDSpider\\spiders')       # 跳到目标路径
if not os.path.exists('JD_Spider.py'): # 看一下这个文件是否存在
    exit(-1)                       #不存在就退出
lines = open('JD_Spider.py').readlines()  #打开文件，读入每一行
JD_Spider = open('F:\\Program_Stores\\Python\\2016-04-26\\Auto\\JDSpider\\JDSpider\\spiders\\JD_Spider.py','w')  #打开需要写入的脚本
for s in lines:
    # replace是替换，write是写入
    JD_Spider.write(s.replace('$$query$$','咖啡'))    
JD_Spider.close()  # 关闭文件


#重写settings.py文件
os.chdir('F:\\Program_Stores\\Python\\2016-04-26\\SpiderModel\\JDSpider\\JDSpider')       # 跳到目标路径
if not os.path.exists('settings.py'): # 看一下这个文件是否存在
    exit(-1)                       #不存在就退出
lines_s = open('settings.py').readlines()  #打开文件，读入每一行
settings = open('F:\\Program_Stores\\Python\\2016-04-26\\Auto\\JDSpider\\JDSpider\\settings.py','w')  #打开需要写入的脚本
for a in lines_s:
    # replace是替换，write是写入
    settings.write(a.replace('$$query$$','咖啡'))    
settings.close()  # 关闭文件