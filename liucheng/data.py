#coding:utf-8
# Time: 2018/11/21 17:09
# Author : WL
import pymysql
#查询89数据库  仓库id和库容量
def cangku():
    name = input('请输入仓库名称:')
    db_89 = pymysql.connect(
                         host="192.168.0.89",
                         port = 3306,
                         user = "web",
                         passwd = "yimaoqiche",
                         db = "tob",
                         charset ='utf8')
    cursor = db_89.cursor()
    sql = ("select id,warehouse_num from tob.tob_goods_warehouse where warehouse_name = '%s'"%name)
    cursor.execute(sql)
    result = cursor.fetchall()
    result1 = str(result)
    # curr_result = result1[3:7]
    # print("251环境手机号码%s的验证码是：%s"%(tel,curr_result))
    print('仓库id、和仓库的库量数为：'+result1)
    cursor.close()

def shouxin():
    #66数据库查询授信ID、联系人、公司、手机号码
    tel = input('请输入手机号码:')

    db_89 = pymysql.connect(
                         host="192.168.0.66",
                         port = 3306,
                         user = "web",
                         passwd = "yimaoqiche",
                         db = "tob_dealer",
                         charset ='utf8')
    cursor = db_89.cursor()
    sql = ("select id,company_name,link_name,link_phone,apply_money,province_id,city_id,district_id,address from tob_dealer.scf_apply_credit where link_phone = %s"%tel)
    cursor.execute(sql)
    result = cursor.fetchall()
    result1 = str(result)
    print('授信ID、联系人、公司、手机号码、申请额度、省、市、区、地址为：'+result1)
    cursor.close()

def gongyingliankucun():
    #66数据库查询供应链金融库存
    tel = input('请输入仓库ID:')

    db_89 = pymysql.connect(
                         host="192.168.0.66",
                         port = 3306,
                         user = "web",
                         passwd = "yimaoqiche",
                         db = "tob_dealer",
                         charset ='utf8')
    cursor = db_89.cursor()
    sql = ("select count(id) from tob_dealer.scf_order_stock where warehouse_id = %s"%tel)
    cursor.execute(sql)
    result = cursor.fetchall()
    result1 = str(result)
    print('供应链金融占用此仓库的库存数为：'+result1)
    cursor.close()
cangku() #通过仓库名称  查询仓库ID、库存  例如：王磊仓库1123
#shouxin()#通过联系人手机  查询授信ID、联系人、公司、手机号码   例如：17610000002
#gongyingliankucun()  #通过仓库ID 查询供应链金融占用此仓库的库存数量  例如：10908
