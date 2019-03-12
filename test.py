#coding:utf-8
# Time: 2018/7/5 17:58
# Author : WL
# a = "19~29岁"
# print(a[0:2])
# print(a[3:5])
# b = "157~165cm"
# print(b[0:3])
# print(b[4:7])
# a=input("请输入一个字符串")
# if a.isdigit():
#     a=int(a)
#     if a>0:
#         if a % 3 ==0 and a % 7 == 0:
#             print("%d可以被3和7整除")%a
#         else:
#             print("不能被3和7整除")
#     else:
#         print("输入的是非正整数")
# else:
#     print("输入的包含非数字")
# a = int(input("请输入一个月份："))
# if a in (1,3,5,7,8,10,12):
#     print("%s月是31天"%a)
# elif a in[2]:
#     print("%s是28天 "%a)
# elif a in [4,6,9,11]:
#     print("%s是30天 "%a)
# else:
#     print("请输入正确的月份")
#
# a = input("请输入一个月份：")
# if a in ('1','3','5','7','8','10','12'):
#     print("%s月是31天"%a)
# elif a in['2']:
#     print("%s是28天 "%a)
# elif a in ['4','6','9','11']:
#     print("%s是30天 "%a)
# else:
#     print("请输入正确的月份")
# print('资料\n95%')
# a = 1
# b = [1,2]
# assert a in b
# params="address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshi"
# params_list=params.split("&")
# user=""
# print(params_list)
# for i in params_list:
#     if i.startswith("username="):
#         #remove是将username=tianlaoshi从params_list中删除
#         params_list.remove(i)
#         #截取tianlaoshi字符串
#         user=i.split("=")[-1]
# print(params_list)
# params_list.sort(reverse=True)
# print(params_list)
# res ="user="+user+"&"+"&".join(params_list)
# print(res)


#coding:utf-8

from appium import webdriver
import time
#
# caps = {
#         "platformName": "Android",
#         "deviceName": "X8QDU15210012328",
#         "platformVersion": "4.4.2",
#         "appPackage": "com.emao.taochemao",
#         "appActivity": "com.emao.taochemao.SplashActivity"
#         # "appWaitActivity": "com.emao.taochemao.GuideActivity"
#         #"appPackage": "com.emao.taochemao",X8QDU15210012328
#         #"appActivity": "com.emao.taochemao.SplashActivity" 5JPDU18327000212
#         #caps["appWaitActivity"] = "com.emao.taochemao.GuideActivity"
#         }
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
#
# size = driver.get_window_size()
# width = size['width']
# height = size['height']
# driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5, 2000)


import os
import time
adb1 = "adb shell input tap 547 1526"
adb2 = "adb shell input tap 485 1380"
i=0
os.system(adb1)
while i < 10000:
    os.system(adb2)
    time.sleep(0.0001)
    i+=1
    print(i)