#coding:utf-8
# Time: 2018/8/24 16:56
# Author : WL
from page.pageelement.pages import *
from common.base import BaseApp
from case.log.loger import Log
log = Log()
import time
class Forgetpwd(BaseApp):
    """登录"""
    def qidong(self):
        """启动图"""
        time.sleep(4)
        self.swipe_qidong_left(n=4)
        a = self.get_title_name(RegisterPage.启动图_立即体验)
        self.click(RegisterPage.启动图_立即体验)
        time.sleep(2)
        log.info("----启动图执行完毕----")
        print("启动执行完毕")
        return a
    def fpwd01(self):
        """校验点击忘记密码，跳转到忘记密码界面"""
        self.click(LoginPage.登录_密码登录)
        self.click(ForgetpwdPage.忘记密码按钮)
        a = self.get_title_name(ForgetpwdPage.忘记密码title)
        log.info("----点击进入忘记密码界面，标题为：%s---"%a)
        print("fpwd01")
        return a
    def fpwd02(self):
        """校验输入空,点击下一步"""
        self.click(ForgetpwdPage.忘记密码_下一步)
        a = self.is_toast_in("手机号")
        log.info("----校验输入空的提示为：%s---"%a)
        print("fpwd02")
        return a
    def fpwd03(self):
        """校验输入空  点击获取验证码"""
        self.click(ForgetpwdPage.忘记密码_获取验证码)
        a = self.is_toast_in("手机号")
        log.info("----校验输入空,点击获取验证码，的提示为：%s---"%a)
        print("fpwd03")
        return a
    def fpwd04(self):
        """校验输入未注册的手机号，获取验证码"""
        self.send_text(ForgetpwdPage.忘记密码_输入手机号,"13812344321")
        self.click(ForgetpwdPage.忘记密码_获取验证码)
        time.sleep(5)
        a = self.get_title_name(ForgetpwdPage.未注册用户找回密码提示语)
        log.info("----校验输入未注册的手机号，获取验证码的提示为：%s---"%a)
        print("fpwd04")
        time.sleep(1)
        self.click(RegisterPage.注册_提示_取消)
        self.clear(ForgetpwdPage.忘记密码_输入手机号)
        return a
    def fpwd05(self):
        """输入非法的手机号，点击获取验证码，提交"""
        self.send_text(ForgetpwdPage.忘记密码_输入手机号,"11111111111")
        self.click(ForgetpwdPage.忘记密码_获取验证码)
        a = self.is_toast_in("手机号")
        log.info("----输入非法的手机号，点击获取验证码的提示为：%s---"%a)
        print("fpwd05")
        self.clear(ForgetpwdPage.忘记密码_输入手机号)
        return a
    def fpwd06(self):
        """输入正确的手机号，点击获取验证码"""
        self.send_text(ForgetpwdPage.忘记密码_输入手机号,"13237888314")
        self.click(ForgetpwdPage.忘记密码_获取验证码)
        # a = self.get_title_name(ForgetpwdPage.忘记密码_获取验证码)
        # log.info("----输入正确的手机号，点击获取验证码的提示为：%s---"%a)
        print("fpwd06")
        return a
    def fpwd07(self):
        """输入正确的手机号，正确的验证码，提交"""
        """校验页面标题"""
        """校验新密码为空，点击完成"""
        """校验两次密码不一致，点击完成"""
        """校验两次密码一致，点击完成"""
        a = self.get_code("13237888314")
        self.send_text(RegisterPage.注册_验证码第一位,a[0])
        self.send_text(RegisterPage.注册_验证码第二位,a[1])
        self.send_text(RegisterPage.注册_验证码第三位,a[2])
        self.send_text(RegisterPage.注册_验证码第四位,a[3])
        self.click(ForgetpwdPage.忘记密码_下一步)
        print("执行下一步")
        time.sleep(5)
        b = self.get_title_name(ForgetpwdPage.设置新密码title)  #获取到设置密码的title
        log.info("----输入正确的手机号，正确的验证码，点击提交，新页面的标题是：%s---"%b)
        self.click(ForgetpwdPage.设置新密码_完成按钮)
        self.click(ForgetpwdPage.设置新密码_完成按钮)
        print("click wancheng")
        c = self.is_toast_in("输入")
        log.info("----设置新密码输入空，点击提交，提示为：%s---"%c)
        self.send_text(ForgetpwdPage.设置新密码_输入新密码,"123456")
        self.send_text(ForgetpwdPage.设置新密码_请再次输入新密码,"0001111111111")
        self.click(ForgetpwdPage.设置新密码_完成按钮)
        d = self.is_toast_in("不相同")
        log.info("----设置两次新密码输入不同，点击提交，提示为：%s---"%d)
        self.clear(ForgetpwdPage.设置新密码_请再次输入新密码)
        self.clear(ForgetpwdPage.设置新密码_输入新密码)
        self.send_text(ForgetpwdPage.设置新密码_输入新密码,"wl123456")
        self.send_text(ForgetpwdPage.设置新密码_请再次输入新密码,"wl123456")
        self.click(ForgetpwdPage.设置新密码_完成按钮)
        self.click(LoginPage.登录_我知道了)
        self.click(LoginPage.登录_知道了)
        self.click(LoginPage.登录_知道了)
        self.click(LoginPage.登录_知道了)
        print("fpwd07")
        return b,c,d
    def exit(self):
        """退出app"""
        self.quit()
if __name__ == '__main__':
    from page import mobile_page
    from appium import webdriver
    info = mobile_page.Mobile()
    LeiDian = info.Reset_chuizi_desired_caps
    driver = webdriver.Remote(info.url, LeiDian)
    a = Forgetpwd(driver)
    a.qidong()
    a.fpwd01()
    a.fpwd02()
    a.fpwd03()
    a.fpwd04()
    a.fpwd06()
    a.fpwd07()
    a.exit()
