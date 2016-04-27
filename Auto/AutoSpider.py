# - * - coding: utf-8 - * -
import os
#处理模板JDSpider
#重写JD_Spider.py文件
os.chdir('F:\\GitRespo\\ShopSpider\\SpiderModel\\JDSpider\\JDSpider\\spiders')       # 跳到模板路径
if not os.path.exists('JD_Spider.py'): # 看一下这个文件是否存在
    exit(-1)                       #不存在就退出
lines = open('JD_Spider.py').readlines()  #打开文件，读入每一行
JD_Spider = open('F:\\GitRespo\\ShopSpider\\Auto\\JDSpider\\JDSpider\\spiders\\JD_Spider.py','w')  #打开需要写入的脚本
for s in lines:
    # replace是替换，write是写入
    JD_Spider.write(s.replace('$$query$$','咖啡'))    
JD_Spider.close()  # 关闭文件


#重写settings.py文件
os.chdir('F:\\GitRespo\\ShopSpider\\SpiderModel\\JDSpider\\JDSpider')   # 跳到模板路径
if not os.path.exists('settings.py'): # 看一下这个文件是否存在
    exit(-1)                       #不存在就退出
lines_s = open('settings.py').readlines()  #打开文件，读入每一行
settings = open('F:\\GitRespo\\ShopSpider\\Auto\\JDSpider\\JDSpider\\settings.py','w')  #打开需要写入的脚本
for a in lines_s:
    # replace是替换，write是写入
    settings.write(a.replace('$$query$$','咖啡'))    
settings.close()  # 关闭文件


#处理模板JDOnePage
#重写JDOnePage.py文件
os.chdir('F:\\GitRespo\\ShopSpider\\SpiderModel\\JDOnepage\\JDOnepage\\spiders')       # 跳到目标路径
if not os.path.exists('JDOnePage.py'): # 看一下这个文件是否存在
    exit(-1)                       #不存在就退出
lines = open('JDOnePage.py').readlines()  #打开文件，读入每一行
JD_Spider = open('F:\\GitRespo\\ShopSpider\\Auto\\JDOnepage\\JDOnepage\\spiders\\JDOnePage.py','w')  #打开需要写入的脚本
for s in lines:
    # replace是替换，write是写入
    JD_Spider.write(s.replace('$$query$$','咖啡'))    
JD_Spider.close()  # 关闭文件


#重写settings.py文件
os.chdir('F:\\GitRespo\\ShopSpider\\SpiderModel\\JDOnepage\\JDOnepage')       # 跳到目标路径
if not os.path.exists('settings.py'): # 看一下这个文件是否存在
    exit(-1)                       #不存在就退出
lines_s = open('settings.py').readlines()  #打开文件，读入每一行
settings = open('F:\\GitRespo\\ShopSpider\\Auto\\JDOnepage\\JDOnepage\\settings.py','w')  #打开需要写入的脚本
for a in lines_s:
    # replace是替换，write是写入
    settings.write(a.replace('$$query$$','咖啡'))    
settings.close()  # 关闭文件