#coding:utf-8
# Time: 2018/9/26 19:29
# Author : WL
from page.RegisterPage import Register
from appium import webdriver
from page import mobile_page
import unittest
from case.log.loger import Log
log = Log()
info = mobile_page.Mobile
LeiDian = info.leidian_desired_caps
url = info.url
class REgister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = webdriver.Remote(url, LeiDian)
        cls.app = Register(driver)
    @classmethod
    def tearDownClass(cls):
        cls.app.exit()
    def test00(self):
       """校验启动图"""
       a = self.app.qidong()
       self.assertEqual(a,"立即体验")
       log.info("--校验向左滑动四次，出现立即体验，并点击成功--")
    def test01(self):
       """校验注册 非空提交"""
       a = self.app.zhuce1()
       self.assertEqual(a,"请输入手机号")
       log.info("--校验注册 非空提交成功--")

    def test02(self):
       """校验手机号码输入异常"""
       try:
           a = self.app.zhuce2()
           self.assertEqual(a,"请输入11位手机号码")
           log.info("--校验手机号码输入异常成功--")
       except Exception:
           print("遇到错误，重新执行")
           a = self.app.zhuce2()
           self.assertEqual(a,"请输入11位手机号码")
           log.info("--校验手机号码输入异常成功--")
       else:
           print("Success")

    def test03(self):
       """校验输入正确的手机号，错误的验证码"""
       a = self.app.zhuce3()
       self.assertEqual(a,"验证码错误")
       log.info("--校验输入正确的手机号，错误的验证码成功--")
    def test04(self):
       """校验输入正确的手机号，3次错误的验证码"""
       try:
           a = self.app.zhuce4()
           self.assertEqual(a,"您的账号已经输入验证码错误三次了，请联系客服处理。")
           log.info("--校验输入正确的手机号，3次错误的验证码成功--")
       except Exception:
           print("出现异常，重新执行")
           a = self.app.zhuce4()
           self.assertEqual(a,"您的账号已经输入验证码错误三次了，请联系客服处理。")
           log.info("--校验输入正确的手机号，3次错误的验证码成功--")
       else:
           print("正常执行")
    def test05(self):
        """校验获取验证码是否正确"""
        a = self.app.zhuce5()
        self.assertEqual(a,"59s")
        log.info("--校验获取验证码是否正确成功--")
    def test06(self):
        """校验进入车商猫的注册页面"""
        a = self.app.zhuce6()
        self.assertEqual(a,"未注册车商猫,将自动为您创建账户")
        log.info("--校验进入车商猫的注册页面成功--")
    def test07(self):
        """校验点击密码登录，跳转到密码登录页面"""
        a = self.app.zhuce7()
        self.assertEqual(a,"验证码登录")
        log.info("--校验点击密码登录，跳转到密码登录页面成功--")
    def test08(self):
        """校验点击验证码登录，跳转到注册页面"""
        a = self.app.zhuce8()
        self.assertEqual(a,"未注册车商猫,将自动为您创建账户")
        log.info("--校验点击验证码登录，跳转到注册页面成功--")
    def test09(self):
        """输入正确的手机号码，输入正确的验证码，点击登录"""
        a = self.app.zhuce9()
        self.assertEqual(a,"知道了")
        log.info("--输入正确的手机号码，输入正确的验证码，点击登录成功--")
        log.info("提示快速管理您的网店成功")
        log.info("提示限时抢购不要错过哦成功")
        log.info("提示上滑查看更多车源哦成功")
if __name__ == '__main__':
        unittest.main()