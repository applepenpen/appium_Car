#coding:utf-8
# Time: 2018/8/15 12:33
# Author : WL
from page.pageelement.pages import *
from common.base import BaseApp
from case.log.loger import Log
log = Log()
import time
class Register(BaseApp):
    """注册"""
    def qidong(self):
        """启动图"""
        time.sleep(10)
        self.swipe_qidong_left(n=2)
        a = self.get_title_name(RegisterPage.启动图_立即体验)
        self.click(RegisterPage.启动图_立即体验)
        log.info("----启动图执行完毕----")
        print("启动执行完毕")
        return a
    def zhuce1(self):
        """校验注册 非空提交"""
        self.click(RegisterPage.注册_登录按钮)
        a = self.is_toast_in("手机")
        log.info("----非空提交的提示语：%s----"%a)
        print("zhuce1")
        return a
    def zhuce2(self):
        """校验手机号码输入异常"""
        self.send_text(RegisterPage.注册_手机号输入框隐藏提示文,"11111111111")
        time.sleep(1)
        self.click(RegisterPage.注册_登录按钮)
        time.sleep(2)
        self.click(RegisterPage.注册_登录按钮)
        print("click login")
        a = self.is_toast_in("11位")
        log.info("----手机号码输入异常的提示语：%s----"%a)
        print("zhuce2")
        return a
    def zhuce3(self):
        """校验输入正确的手机号，错误的验证码"""
        self.find(RegisterPage.注册_手机号输入框隐藏提示文).clear()
        self.send_text(RegisterPage.注册_手机号输入框隐藏提示文,"13237888314")
        self.send_text(RegisterPage.注册_验证码第一位,1)
        self.send_text(RegisterPage.注册_验证码第二位,1)
        self.send_text(RegisterPage.注册_验证码第三位,1)
        self.send_text(RegisterPage.注册_验证码第四位,1)
        self.click(RegisterPage.注册_登录按钮)
        a = self.is_toast_in("错误")
        log.info("----输入正确的手机号，错误的验证码的提示语：%s----"%a)
        print("zhuce3")
        return a
    def zhuce4(self):
        """校验输入正确的手机号，3次错误的验证码"""
        for i in range(2):
            self.click(RegisterPage.注册_登录按钮)
            time.sleep(2)
        a = self.is_toast_in("错误三次了")
        log.info("----输入正确的手机号，输入三次错误的验证码的提示语：%s----"%a)
        time.sleep(1)
        self.click(RegisterPage.注册_提示_取消)
        time.sleep(1)
        print("zhuce4")
        return a
    def zhuce5(self):
        """校验获取验证码是否正确"""
        #***********调试代码*********************
        # self.send_text(RegisterPage.注册_手机号输入框隐藏提示文,"15848414299")
        #***********调试代码*********************
        self.click(RegisterPage.注册_获取验证码)
        print("click code")
        print("zhuce5")
    def zhuce6(self):
        """校验进入车商猫的注册页面"""
        a = self.get_title_name(RegisterPage.注册_未注册车商猫提示)
        log.info("----未注册车商猫提示：%s----"%a)
        print("zhuce6")
        return a
    def zhuce7(self):
        """校验点击密码登录，跳转到密码登录页面"""
        self.click(RegisterPage.注册_密码登录按钮)
        a = self.get_title_name(LoginPage.登录_验证码登录)
        log.info("----跳转登录页面成功----")
        print("zhuce7")
        return a
    def zhuce8(self):
        """校验点击验证码登录，跳转到注册页面"""
        self.click(LoginPage.登录_验证码登录)
        a = self.get_title_name(RegisterPage.注册_未注册车商猫提示)
        log.info("----跳转注册录页面成功----")
        print("zhuce8")
        return a
    def zhuce9(self):
        """输入正确的手机号码，输入正确的验证码，点击登录"""
        self.click(RegisterPage.注册_获取验证码)
        time.sleep(5)
        a = self.get_code(13237888314)
        self.send_text(RegisterPage.注册_验证码第一位,a[0])
        self.send_text(RegisterPage.注册_验证码第二位,a[1])
        self.send_text(RegisterPage.注册_验证码第三位,a[2])
        self.send_text(RegisterPage.注册_验证码第四位,a[3])
        time.sleep(1)
        self.click(RegisterPage.注册_登录按钮)
        time.sleep(2)
        b = self.is_element_exist(LoginPage.登录_我知道了)
        self.click(LoginPage.登录_我知道了)  #提示快速管理您的网店
        time.sleep(1)
        c = self.is_element_exist(LoginPage.登录_知道了)
        self.click(LoginPage.登录_知道了)  #提示限时抢购不要错过哦
        time.sleep(1)
        d = self.is_element_exist(LoginPage.登录_知道了)
        self.click(LoginPage.登录_知道了)  #提示上滑查看更多车源哦
        e = self.is_element_exist(LoginPage.登录_知道了)
        self.clear(LoginPage.登录_知道了)
        f = self.get_title_name(LoginPage.登录_首页title)
        log.info("登录成功的关键词是：%s"%f)
        print("zhuce9")
        return b,c,d,e,f
    def exit(self):
        """退出app"""
        self.quit()
if __name__ == '__main__':
    from page import mobile_page
    from appium import webdriver
    info = mobile_page.Mobile()
    HuaWei = info.Reset_chuizi_desired_caps
    driver = webdriver.Remote(info.url, HuaWei)
    print('启动车商猫')
    a = Register(driver)
    a.qidong()
    a.zhuce1()
    a.zhuce2()
    a.zhuce3()
    a.zhuce4()
    a.zhuce5()
    a.zhuce6()
    a.zhuce7()
    a.zhuce8()
    a.zhuce9()
    a.exit()


