# coding:utf-8
import yaml
import os
curpath = os.path.dirname(os.path.realpath(__file__))
pagepath = os.path.join(curpath, "pageelement", "register_page.yaml")
# yamlpath = os.path.join(pagepath, "pageelement",  "config_setting_page")
f = open(pagepath , "r", encoding="utf-8")
# f = open("config_setting_page.111yaml",'r',encoding="utf-8")
a = f.read()
f.close()
print(a)

# 把yaml文件转字典
d = yaml.load(a)
print(d)

# print(d["RegisterMenPage"]['desc'])
# for i in d["ConfigSettingPage"]['locators']:
#
#
#  """写一个，根据page页面，和name值找到定位方法（by ,value)"""
# def get_locator(name):
#     locs = d["ConfigSettingPage"]['locators']  # 返回list
#     for i in locs:
#         if name == i['name']:
#             return i
# #
# if __name__ == "__main__":
#     pass






