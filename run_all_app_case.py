# coding=utf-8

from common import HTMLTestRunner_cn
import unittest
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
cur_path = os.path.realpath(__file__)  #获取当前脚本地址
forward = os.path.dirname(cur_path)    #获取文件夹地址
casedir = os.path.join(forward,"case")    #拼接用例地址
reportdir = os.path.join(forward,"report") #拼接测试报告地址
print(cur_path,forward,casedir,reportdir)

def add_case(): #第一步：加载所有测试用例
    if not os.path.exists(casedir):os.mkdir(casedir) #如果没有该文件，重新创建
    print("测试用例的路径为:%s"%casedir)
discover = unittest.defaultTestLoader.discover(start_dir=casedir,pattern='test*.py',top_level_dir=None)
print(discover)
def run_case():
    """第二步：执行所有测试用例，并把结果写入到HTML测试报告"""
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    #如果测试报告文件夹不存在，创建一个
    if not os.path.exists(reportdir):os.mkdir(reportdir)
    time1 = now +"result.html"
    report_abspath = os.path.join(reportdir,time1)
    print('最新的测试报告的路径为:%s'%report_abspath)
    fp = open(report_abspath,"wb")
    runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='车商猫自动化测试',description='用例执行情况:',verbosity=2,retry=1)
    runner.run(discover)
    fp.close()

if __name__ == '__main__':
    add_case()  #加载所有用例
    run_case()  #运行所有用例
    # runner =unittest.TextTestRunner()
    # sendmail()
    # print("\n老韩测试报告已发送至您的邮箱，请查收")

# '''
# import unittest
# import time
# from common import HTMLTestRunner_cn
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import os
# # 当前脚本所在文件真实路径
# cur_path = os.path.dirname(os.path.realpath(__file__))
# print(cur_path)
# def add_case(caseName="case", rule="test*.py"):
#     '''第一步：加载所有的测试用例'''
#     case_path = os.path.join(cur_path, caseName)  # 用例文件夹
#     # 如果不存在这个case文件夹，就自动创建一个
#     if not os.path.exists(case_path):os.mkdir(case_path)
#     print("test case path:%s"%case_path)
#     # 定义discover方法的参数
#     discover = unittest.defaultTestLoader.discover(case_path,
#                                                   pattern=rule,
#                                                   top_level_dir=None)
#     print(discover)
#     return discover
#
# def run_case(all_case, reportName="report"):
#     '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
#     now = time.strftime("%Y_%m_%d_%H_%M_%S")
#     report_path = os.path.join(cur_path, reportName)  # 用例文件夹
#     # 如果不存在这个report文件夹，就自动创建一个
#     if not os.path.exists(report_path):os.mkdir(report_path)
#     time1 = now +"result.html"
#     report_abspath = os.path.join(report_path, time1)
#     print("report path:%s"%report_abspath)
#     fp = open(report_abspath, "wb")
#     runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
#                                                verbosity=3,
#                                                title='车商猫自动化测试报告,测试结果如下：',
#                                                description='用例执行情况：')
#
#     # 调用add_case函数返回值
#     runner.run(all_case)
#     fp.close()
#
# def get_report_file(report_path):
#     '''第三步：获取最新的测试报告'''
#     lists = os.listdir(report_path)
#     lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
#     print (u'最新测试生成的报告： '+lists[-1])
#     # 找到最新生成的报告文件
#     report_file = os.path.join(report_path, lists[-1])
#     return report_file
#
# def send_mail(sender, psw, receiver, smtpserver, report_file, port):
#     '''第四步：发送最新的测试报告内容'''
#     with open(report_file, "rb") as f:
#         mail_body = f.read()
#     # 定义邮件内容
#     msg = MIMEMultipart()
#     body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
#     msg['Subject'] = "自动化测试报告"
#     msg["from"] = sender
#     msg["to"] = ",".join(receiver)     # 只能字符串
#     msg.attach(body)
#     # 添加附件
#     att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename= "report.html"'
#     msg.attach(att)
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)                      # 连服务器
#         smtp.login(sender, psw)
#     except:
#         smtp = smtplib.SMTP_SSL(smtpserver, port)
#         smtp.login(sender, psw)                       # 登录
#     smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.quit()
#     print('test report email has send out !')
#
# if __name__ == "__main__":
#     all_case = add_case()   # 1加载用例
#     # # 生成测试报告的路径
#     run_case(all_case)        # 2执行用例
#     # # 获取最新的测试报告文件
#     report_path = os.path.join(cur_path, "report")  # 用例文件夹
#     report_file = get_report_file(report_path)  # 3获取最新的测试报告
#     # #邮箱配置
#     sender = "313035600@qq.com"
#     psw = "wl888888"
#     smtp_server = "smtp.qq.com"
#     port = 465
#     receiver = "6148694@qq.com"
#     # send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告
#
# '''
