#coding:utf-8
import MySQLdb
import string
import json

class kang:
    def __init__(self,filename):
        self.filename = filename
        self.num_list = []
        self.conn = MySQLdb.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '123456',
            db = 'imooc',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor()
        # print self.conn
        # print self.cursor

    def read_file(self):
        for line in open(self.filename):
            # print "取出的文本"
            # print line
            self.process_raw_world(line)




    #获取了各字段的值
    # ===========================================need to be changed===========================
    def process_raw_world(self,line):
        # print type(line)
        dict1 = json.loads(line)
        # print dict1["id"].encode('utf-8')
        # print dict1["xianjia"].encode('utf-8')
        # print dict1["yuanjia"].encode('utf-8')
        self.num_list = []#此处要清空列表，否则会产生叠加
        print "取出一个商品-----------------------------》"
        self.num_list.append(string.atoi(dict1["id"]))
        self.num_list.append(string.atof(dict1["yuanjia"]))
        self.num_list.append(string.atof(dict1["xianjia"]))

        print type(self.num_list[0])
        print type(self.num_list[1])
        print type(self.num_list[2])
        # print self.num_list.__len__()
        # print self.num_list[0]
        #如果这一纪录不在数据库才插入
        sql = "insert into muying_price values (%u,%f,%f)" % tuple(self.num_list)
        if self.isResist(self.num_list[0]) == 0:

            # sql = "insert into phone_details values (2020064.0, 5.0, 0.0, 0.945, 3.0, 4.0, 0.026, 94.0, 0.029, 3.0, 142.0, 1220064.0, 38288.0, 2610.0, 4.0, 40898.0, 1160.0, 1160.0, 934.0, 43357.0, 5402.0, 1299.0, 0.0, 365.0);"
            print sql
            ret = self.cursor.execute(sql)
            self.conn.commit()
            if ret == 0:
                pass
            else:
                self.conn.commit()


    #负责关闭连接对象的游标
    def destr(self):

        self.cursor.close()
        self.conn.close()

    #判断该记录是否存在，存在返回1，不存在返回0
    # ===========================================need to be changed===========================
    def isResist(self,num):
        sql = "select * from muying_price where id = %u"%num
        re = self.cursor.execute(sql)

        print re
        if re == 0:
            print "不存在"
            return 0
        else:
            print int(num)
            print "已经存在"
            return  1



#===========================================need to be changed===========================
if __name__ == "__main__":
    too = kang("muying_all_feature.txt")
    too.read_file()
    too.destr()


