#coding:utf-8
# Time: 2019/1/18 12:27
# Author : WL
import tkinter
import pymysql
top = tkinter.Tk()
top.title('电子名片删除账号')
label = tkinter.Label(top,text = '适用于测一、灰度')
label.pack()
varRst = tkinter.StringVar()
var = tkinter.StringVar(value="请输入手机号码：")
edit = tkinter.Entry(top,width = 55,textvariable = var)
edit.pack()
result = tkinter.Button(top,text = '删除测一账号',bg = 'white',fg = 'black',width = 15)
result.pack()
result2 = tkinter.Button(top,text = '删除灰度账号',bg = 'white',fg = 'black',width = 15)
result2.pack()
def delete_test1_cart(event):
    try:
        mobile = str(edit.get())
        connect = pymysql.Connect(host='192.168.0.66',port=3306,user='web',passwd='yimaoqiche',db='cart',charset='utf8')#连接测试一数据库
        cursor = connect.cursor()#获取游标
        #select_id_sql = "SELECT id FROM cart_user where phone = %s"
        select_id_sql = "DELETE FROM cart_user where id =195"
        #cursor.execute(select_id_sql%mobile)
        cursor.execute(select_id_sql)
        id_value = str(cursor.fetchall())
        New_id_value = id_value[2:5]
        print(New_id_value)
        delete_sql1 = 'DELETE FROM cart_user where id = %s'
        cursor.execute(delete_sql1%New_id_value)
        print('删除电子名片账号成功')
        delete_sql2 = 'DELETE FROM cart_user_behavior where check_id not in (SELECT id from cart_user where deleted_at is NULL)'
        cursor.execute(delete_sql2)
        print('猫哥卫星垃圾数据清除')
        delete_sql3 = 'DELETE FROM cart_user_behavior where user_id = %s'
        cursor.execute(delete_sql3%New_id_value)
        print('删除猫哥卫星记录成功')
        delete_sql4 = 'DELETE FROM cart_business_circle where user_id not in (SELECT id from cart_user where deleted_at is NULL)'
        cursor.execute(delete_sql4)
        print('清除车商圈垃圾数据成功')
        connect.close()
        var.set("恭喜您，清除账号成功！")
    except:
        var.set("请正确输入手机号码！")
def delete_huidu_cart(event):
    try:
        mobile = str(edit.get())
        connect = pymysql.Connect(host='47.93.180.145',port=3306,user='web',passwd='yimaoqiche',db='cart',charset='utf8')#连接测试一数据库
        cursor = connect.cursor()#获取游标
        select_id_sql = "SELECT id FROM cart_user where phone = %s"
        delete_sql1 = "DELETE FROM cart_user where id = %s"
        delete_sql2 = "DELETE FROM cart_user_behavior where check_id not in (SELECT id from cart_user where deleted_at is NULL)"
        delete_sql3 = "DELETE FROM cart_user_behavior where user_id = %s"
        delete_sql4 = "DELETE FROM cart_business_circle where user_id not in (SELECT id from cart_user where deleted_at is NULL)"
        cursor.execute(select_id_sql%mobile)
        id_value = str(cursor.fetchall())
        New_id_value = id_value[2:5]
        print(New_id_value)
        cursor.execute(delete_sql1%New_id_value)
        print('通过ID删除账号成功')
        cursor.execute(delete_sql2)
        print('清除猫哥卫星成功')
        cursor.execute(delete_sql3%New_id_value)
        print('删除猫哥卫星记录成功')
        cursor.execute(delete_sql4)
        print('清除车商圈垃圾数据成功')
        connect.close()
        var.set("恭喜您，清除账号成功！" )
    except:
        var.set("请正确输入手机号码！！！！")
result.bind('<Button-1>',delete_test1_cart)
result2.bind('<Button-1>',delete_huidu_cart)
tkinter.mainloop()