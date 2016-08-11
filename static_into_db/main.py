#coding:utf-8
import MySQLdb
import string

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
            if line != '' and line.find('@') != -1:
                print "取出的文本"
                print line
                self.process_raw_world(line)

    #获取了各字段的值
    # ===========================================need to be changed===========================
    def process_raw_world(self,line):
        # print type(line)
        self.num_list = []#此处要清空列表，否则会产生叠加
        tokens = line.split('@')
        num = 0
        for dev in tokens:
            if dev == tokens[1]:
                # print "第一个项目"
                # print dev
                # print dev.split()[1]
                # print string.atoi(dev.split()[1])
                # print type(string.atoi(dev.split()[1]))
                self.num_list.append(string.atoi(dev.split()[1]))
                # print "插入"
                continue
            else :
                if  dev != '':
                    # print dev.strip()
                    ll = dev.strip().split()
                    # print string.atof(ll[1])
                    # print dev
                    # print dev.find('\n')
                    if ll[1].find('\n') != -1:
                        temp_str=ll[1].replace('\n','')
                        self.num_list.append(string.atof(temp_str))
                        # print "插入"
                    else:
                        self.num_list.append(string.atof(ll[1]))
                        # print "插入"

        #如果这一纪录不在数据库才插入
        print len(self.num_list)
        sql = "insert into muying_details_copy values (%u,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)" % tuple(self.num_list)
        if self.isResist(self.num_list[0]) == 0:
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
        sql = "select * from muying_details_copy where productId = %u"%num
        re = self.cursor.execute(sql)
        print re
        if re == 0:
            print "已经存在"
            return 0
        else:
            print int(num)
            print "已经存在"
            return  1



#===========================================need to be changed===========================
if __name__ == "__main__":
    too = kang("muying_comment__static.txt")
    too.read_file()
    too.destr()


