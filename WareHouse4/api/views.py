# Create your views here.

from rest_framework.decorators import api_view
from utils.jsonformat import reslistif, resAlllistif


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
    newsql =  "select * from System_Users where Mobile = '"+Phone+"'"
    print(newsql)
    return reslistif(newsql)

# 全部数据
@api_view(['GET', 'POST'])
def GetAllList(req,format=None):
    if req.method == 'GET':
        # Phone = req.GET["Phone"]
        cangkuid = req.GET['cangkuid']
    elif req.method == 'POST':
        # Phone=  req.POST['Phone']
        cangkuid = req.POST['cangkuid']
    newsql1 = "select * from Stock_IN"
    newsql2 = "select * from Stock_IN_Detail"
    newsql3 = "select * from Stock_OUT"
    # newsql4 = "select * from Stock_OUT_Detail"
    newsql5 = "select * from Stock_CHECK"
    newsqlList={"Stock_IN":newsql1,"Stock_IN_Detail":newsql2,"Stock_OUT":newsql3,"Stock_CHECK":newsql5}
    # print(newsql)
    return resAlllistif(newsqlList)
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