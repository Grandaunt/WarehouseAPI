#!/usr/bin/python3
# Create your views here.

from rest_framework.decorators import api_view

from utils.db import MSSQL
from utils.jsonformat import reslistif, resAlllistif, validationMD5, json_error


# http://wms.bjszhgx.com/api/receive/userlogin?{"PassWord":"123456","Phone":"18610056339"}
# {"Status":200,"Msg":"成功","Data":{System_User}}
# 登录
@api_view(['GET', 'POST'])
def UserLogin(req,format=None):
    if req.method == 'GET':
        Phone = req.GET["Phone"]
        PassWord = req.GET['PassWord']
    elif req.method == 'POST':
        Phone=  req.POST['Phone']
        PassWord = req.POST['PassWord']
    newsql0 =  "select LoginKey from System_Users where Mobile = '"+Phone+"'"
    ms = MSSQL()
    reslist = ms.ExecQuery(newsql0.encode('utf-8'))
    print(reslist)
    PassWord=validationMD5(reslist.get("LoginKey"),PassWord,"UTF-16")
    newsql1 = "select * from System_Users where Mobile = '" + Phone + "' and LoginPwd = '"+PassWord+"'"
    return reslistif(newsql1)

# 全部数据
@api_view(['GET', 'POST'])
def GetAllList(req,format=None):
    privateKey = "202CA26E33226DC"
    if req.method == 'GET':
        userid = req.GET["userid"]
        cangkuid = req.GET['cangkuid']
        md5 = req.GET['md5']
    elif req.method == 'POST':
        userid=  req.POST['userid']
        cangkuid = req.POST['cangkuid']
        md5 = req.POST['md5']
    if validationMD5(userid+cangkuid,privateKey,"UTF-8")==md5:
        print("MD5验证成功")
        newsql0 = "select * from System_Users where UserId = '"+userid+"' and RoleId <= '3'"
        ms = MSSQL()
        reslist = ms.ExecQuery(newsql0.encode('utf-8'))
        if reslist:#判断用户角色权限
            newsql1 = "select * from Stock_IN"
            newsql2 = "select * from Stock_IN_Detail"
            newsql3 = "select * from Stock_OUT"
            newsql4 = "select * from Stock_OUT_Detail"
            newsql5 = "select * from Stock_CHECK"
            newsql6 = "select * from Stock_CHECK_Detail"
            newsqlList={"Stock_IN":newsql1,"Stock_IN_Detail":newsql2,"Stock_OUT":newsql3,"Stock_OUT_Detail":newsql4,"Stock_CHECK":newsql5,"Stock_CHECK_Detail":newsql6}
        # print(newsql)
        return resAlllistif(newsqlList)
    else:
        return json_error()
# 入库单
@api_view(['GET', 'POST'])
def GetStockinList(req,format=None):
    if req.method == 'GET':
        # InNumber = req.GET['innumber']
        cangkuid = req.GET['cangkuid']
        # inNumber = req.GET['inNumber']
    elif req.method == 'POST':
        # InNumber=  req.POST['innumber']
        cangkuid = req.POST['cangkuid']
        # inNumber = req.POST['inNumber']

    # http: // 127.0.0.1: 8000 / getstockinlist /?userid = 180304172258534 & cangkuid = 10
    newsql =  "select * from Stock_IN"
    # newsql =  "select * from Stock_IN where InNumber = '"+InNumber+"'"+"and CangKuId = '"+cangkuid+"'"
    print(newsql)
    return reslistif(newsql)
    # return HttpResponse(json.dumps(reslist, cls=DateEncoder,default=json_data), content_type='application/json')
     # return reslistif(newsql)


# 入库详细单
@api_view(['GET', 'POST'])
def GetStockInDetailList(req,format=None):
    if req.method == 'GET':
        # innumber = req.GET['innumber']
        cangkuid = req.GET['cangkuid']
        # inNumber = req.GET['inNumber']
    elif req.method == 'POST':
        # innumber=  req.POST['innumber']
        cangkuid = req.POST['cangkuid']
        # inNumber = req.POST['inNumber']

    # http: // 127.0.0.1: 8000 / getstockinlist /?userid = 180304172258534 & cangkuid = 10
    newsql =  "select * from Stock_IN_Detail"
    # newsql =  "select * from Stock_IN_Detail where InNumber = '"+innumber+"'"+"and CangKuId = '"+cangkuid+"'"
    print(newsql)
    return reslistif(newsql)

# 出库单
@api_view(['GET', 'POST'])
def GetStockOutList(req,format=None):
    if req.method == 'GET':
        # OutNumber = req.GET['outnumber']
        cangkuid = req.GET['cangkuid']
        # inNumber = req.GET['inNumber']
    elif req.method == 'POST':
        # OutNumber=  req.POST['outnumber']
        cangkuid = req.POST['cangkuid']
        # inNumber = req.POST['inNumber']

    # http: // 127.0.0.1: 8000 / getstockinlist /?userid = 180304172258534 & cangkuid = 10
    newsql =  "select * from Stock_OUT"
    # newsql =  "select * from Stock_OUT where OutNumber = '"+OutNumber+"'"+"and CangKuId = '"+cangkuid+"'"
    print(newsql)
    return reslistif(newsql)

# 出库详细单
@api_view(['GET', 'POST'])
def GetStockOutDetailList(req,format=None):
    if req.method == 'GET':
        # OutNumber = req.GET['outnumber']
        cangkuid = req.GET['cangkuid']
        # inNumber = req.GET['inNumber']
    elif req.method == 'POST':
        # OutNumber=  req.POST['outnumber']
        cangkuid = req.POST['cangkuid']
        # inNumber = req.POST['inNumber']

    # http: // 127.0.0.1: 8000 / getstockinlist /?userid = 180304172258534 & cangkuid = 10
    newsql =  "select * from Stock_OUT_Detail"
    # newsql =  "select * from Stock_OUT_Detail where OutNumber = '"+OutNumber+"'"+"and CangKuId = '"+cangkuid+"'"
    print(newsql)
    return reslistif(newsql)


# 盘点单
@api_view(['GET', 'POST'])
def GetStockCheckList(req,format=None):
    if req.method == 'GET':
        # CheckNumber = req.GET['checknumber']
        cangkuid = req.GET['cangkuid']
        # inNumber = req.GET['inNumber']
    elif req.method == 'POST':
        # CheckNumber=  req.POST['checknumber']
        cangkuid = req.POST['cangkuid']
        # inNumber = req.POST['inNumber']

    # http: // 127.0.0.1: 8000 / getstockinlist /?userid = 180304172258534 & cangkuid = 10
    newsql =  "select * from Stock_CHECK"
    # newsql =  "select * from Stock_CHECK where CheckNumber = '"+CheckNumber+"'"+"and CangKuId = '"+cangkuid+"'"
    print(newsql)
    return reslistif(newsql)


# 盘点详细单
@api_view(['GET', 'POST'])
def GetStockCheckDetailList(req,format=None):
    if req.method == 'GET':
        # CheckNumber = req.GET['checknumber']
        cangkuid = req.GET['cangkuid']
        # inNumber = req.GET['inNumber']
    elif req.method == 'POST':
        # CheckNumber=  req.POST['checknumber']
        cangkuid = req.POST['cangkuid']
        # inNumber = req.POST['inNumber']

    # http: // 127.0.0.1: 8000 / getstockinlist /?userid = 180304172258534 & cangkuid = 10
    newsql =  "select * from Stock_CHECK_Detail"
    # newsql =  "select * from Stock_CHECK_DetailList where CheckNumber = '"+CheckNumber+"'"+"and CangKuId = '"+cangkuid+"'"
    print(newsql)
    return reslistif(newsql)