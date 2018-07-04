#!/user/bin/env python
# -*_ coding:utf-8 -*-
# by Havoc
import datetime
import decimal

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
         print(newsqldict.keys())
         print(j)
         data[j]=reslist
         # print(data)
    if data:
        return json_success(data)
        # reslist = json_success(reslist)
    else:
        return json_error(data)

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
        return dict(year=value.year, month=value.month, day=value.day)
    elif isinstance(value, decimal.Decimal):
          return float(value)
    else:
        return value.__dict__