#!/user/bin/env python
# -*_ coding:utf-8 -*-
# by Havoc
import pymssql


class MSSQL:
    def __init__(self, host="120.27.107.11", user="sa", pwd= "bj160630sjs", db="WmsDB"):
            self.host = host
            self.user = user
            self.pwd = pwd
            self.db = db
    #         self.host = "120.27.107.11"
    #         self.user = "sa"
    #         self.pwd = "bj160630sjs"
    #         self.db = "WmsDB"

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="GBK")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]


        if len(resList)>1:    # //多条数据
            result = []
            for row in resList:
                objDict = {}
                # 把每一行的数据遍历出来放到Dict中
                for index, value in enumerate(row):
                    index, col_names[index], value
                    objDict[col_names[index]] = value
                result.append(objDict)
        elif len(resList)>0: # 单条数据
             result={}
             row=resList[0]
             objDict = {}
             # 把每一行的数据遍历出来放到Dict中
             for index, value in enumerate(row):
                index, col_names[index], value
                objDict[col_names[index]] = value
             result=objDict
        else:
            result = {}
        # 查询完毕后必须关闭连接
        self.conn.close()
        return result

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


# ms = MSSQL(host="192.168.1.1",user="sa",pwd="sa",db="testdb")
# ms = MSSQL(host="120.27.107.11", user="sa", pwd="bj160630sjs", db="WmsDB")
#测试数据
ms = MSSQL()
newsql = "select * from System_Users where Mobile = '18610056339'"
reslist = ms.ExecQuery(newsql.encode('gb2312'))
for i in reslist:
    print(i)