#coding:utf-8
# Time: 2019/1/18 10:23
# Author : WL
import tkinter
import pymysql
top = tkinter.Tk()
top.title('手机验证码查询')
label = tkinter.Label(top,text = '适用于测一、灰度、线上')
label.pack()
varRst = tkinter.StringVar()
labelResult = tkinter.Label(top,textvariable = varRst,fg = 'black')
labelResult2 = tkinter.Label(top,textvariable = varRst,fg = 'black')
labelResult3 = tkinter.Label(top,textvariable = varRst,fg = 'black')
var = tkinter.StringVar(value="请输入手机号码：")
edit = tkinter.Entry(top,width = 55,textvariable = var)
edit.pack()
result = tkinter.Button(top,text = '查询测一验证码',bg = 'white',fg = 'black',width = 15)
result.pack()
result2 = tkinter.Button(top,text = '查询灰度验证码',bg = 'white',fg = 'black',width = 15)
result2.pack()
result3 = tkinter.Button(top,text = '查询线上验证码',bg = 'white',fg = 'black',width = 15)
result3.pack()
def findtest1Code(event):
    try:
        labelResult.pack()
        mobile = str(edit.get())
        connect = pymysql.Connect(host='192.168.0.123',port=3306,user='web',passwd='yimaoqiche',db='tob',charset='utf8')#连接测试一数据库
        cursor = connect.cursor()#获取游标
        sql = "SELECT str_content  FROM tob.tob_sms WHERE phone=%s ORDER BY id DESC LIMIT 1 "
        cursor.execute(sql%mobile)
        code = cursor.fetchall()
        print(code)
        connect.close()
        var.set(code)
        labelResult.pack()
    except:
        var.set("请正确输入手机号码")
def findhuiduCode(event):
    try:
        labelResult.pack()
        mobile = str(edit.get())
        connect = pymysql.Connect(host='123.57.216.251',port=3306,user='web',passwd='yimaoqiche',db='tob',charset='utf8')#连接测试一数据库
        cursor = connect.cursor()#获取游标
        sql = "SELECT str_content  FROM tob.tob_sms WHERE phone=%s ORDER BY id DESC LIMIT 1 "
        cursor.execute(sql%mobile)
        code = cursor.fetchall()
        print(code)
        connect.close()
        var.set(code)
        labelResult.pack()
    except:
        var.set("请正确输入灰度环境的手机号码")
def findonlineCode(event):
    try:
        labelResult.pack()
        mobile = str(edit.get())
        connect = pymysql.Connect(host='123.57.37.221',port=5044,user='rd',passwd='readonly',db='tob',charset='utf8')#连接测试一数据库
        cursor = connect.cursor()#获取游标
        sql = "SELECT str_content  FROM tob.tob_sms WHERE phone=%s ORDER BY id DESC LIMIT 1 "
        cursor.execute(sql%mobile)
        code = cursor.fetchall()
        print(code)
        connect.close()
        var.set(code)
        labelResult.pack()
    except:
        var.set("请正确输入线上环境的手机号码")
labelResult.pack()
result.bind('<Button-1>',findtest1Code)
result2.bind('<Button-1>',findhuiduCode)
result3.bind('<Button-1>',findonlineCode)
tkinter.mainloop()