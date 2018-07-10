#!/user/bin/env python
# -*_ coding:utf-8 -*-
# by Havoc
import datetime
import decimal
import hashlib

import simplejson
from django.http import HttpResponse
from rest_framework.utils import json
from dss.Serializer import serializer
from utils.db import MSSQL
import json
# def json_response(data, code=200, foreign_penetrate=False, **kwargs):
#     data = { "code": code, "msg": "成功", "data": data, }
#     return response_as_json(data, foreign_penetrate=foreign_penetrate)
# def json_error(error_string="", code=500, **kwargs):
#     data = { "code": code, "msg": error_string, "data": {} }
#     data.update(kwargs)
#     return response_as_json(data)

def json_success(data, code=200, foreign_penetrate=False, **kwargs):
    data = {
        "Status": code,
        "Msg": "成功",
        "Data": data,
    }
    print(data)
    return response_as_json(data, foreign_penetrate=foreign_penetrate)


def json_error(code=500,error_string="失败", **kwargs):
    data = {
        "Status": code,
        "Msg": error_string,
        "Data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

# def response_as_json(data, foreign_penetrate=False):
#     jsonString = serializer(data=data, output_type="json", foreign=foreign_penetrate)
#     response = HttpResponse(
#           # json.dumps(dataa, cls=MyEncoder),
#          jsonString,
#          content_type="application/json",
#         )
#     response["Access-Control-Allow-Origin"] = "*"
#     return response

def response_as_json(data, foreign_penetrate=False):
    # jsonString = serializer(data=data, output_type="json")
    # print("jsonString"+jsonString)
    # response =HttpResponse(json.dumps(data,  default=lambda obj: obj.__dict__), content_type='application/json')
    return HttpResponse(json.dumps(data, cls=DateEncoder,default=json_data), content_type='application/json')
    # return response

def reslistif(newsql):
    ms = MSSQL()
    reslist = ms.ExecQuery(newsql.encode('utf-8'))
    if reslist:
        return json_success(reslist)
        # reslist = json_success(reslist)
    else:
        return json_error(reslist)
        # reslist = json_error(reslist)
        # return reslist
        # return HttpResponse(json.dumps(reslist,), content_type='application/json')





def resAlllistif(newsqldict):
    ms = MSSQL()
    # print(newsqldict.values())
    data={}
    for j ,i in newsqldict.items():
         reslist = ms.ExecQuery(i.encode('utf-8'))
         # print(newsqldict.keys())
         # print(j)
         if len(reslist)<=0 :  #无结果
             data[j] = []
         elif isinstance(reslist,list):#多条结果
             data[j]=reslist
         else:  #isinstance(reslist,dict)#单条结果
             ilist = []
             ilist.append(reslist)
             data[j] = ilist

         # print(data)
        # if data:
    if data:
        return json_success(data)
        # reslist = json_success(reslist)
    else:
        return json_error(data)

# # 约定好的验证方法
# def validationRole(data):
#     if data.get("UerRole")==3:
#         return True;
#
#     else:
#         return False;


# MD5加密规则 = userid + 密钥 + 仓库ID
def validationMD5(ystr,privateKey,encoding):
    # privateKey = "202CA26E33226DC"
    vmd5=ystr+privateKey
    # 创建md5对象
    hl = hashlib.md5()
    print('MD5加密前为 ：' + vmd5)
    if encoding=="UTF-16":
        hl.update(vmd5.encode(encoding='UTF-16'))
        print('MD5加密后为 ：' + hl.hexdigest())
    elif encoding=="UTF-8":
        hl.update(vmd5.encode(encoding='UTF-8'))
        print('MD5加密后为 ：' + hl.hexdigest())
    elif encoding=="GBK":
        hl.update(vmd5.encode(encoding='GBK'))
        print('MD5加密后为 ：' + hl.hexdigest())
    elif encoding=="GB2312":
        hl.update(vmd5.encode(encoding='GB2312'))
        print('MD5加密后为 ：' + hl.hexdigest())
    # 898c71020ad4b413b242d52f02e4c620
    # vmd5=hl.hexdigest()
    # print(vmd5)
    # if ymd5==ymd5:
    #      return True;
    #         # MD5加密规则 = userid + 密钥 + 仓库ID
    # else:
    return hl.hexdigest();

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

def json_data(value):
    if isinstance(value, datetime.date):
        # print(str(value.year)+"-"+str(value.month)+"-"+str(value.day))
        # return dict(year=value.year, month=value.month, day=value.day)
        return str(value.year)+"-"+str(value.month)+"-"+str(value.day)
    elif isinstance(value, decimal.Decimal):
          return float(value)
    else:
        return value.__dict__