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
                # print "取出的文本"
                # print 'line:', line
                # print line[:-3]
                # print line.find( '\xa8')
                # print list(line)

                self.process_raw_world(line)

    #获取了各字段的值
    def process_raw_world(self,line):
        self.num_list = []#此处要清空列表，否则会产生叠加
        tokens = line.split('@')
        id = string.atoi(tokens[1])

        name = tokens[2]
        new_list = list(name)
        changed =  "".join(new_list)
        temp_list =  changed




        # print "加工前的名称字符串"
        # print list(temp_list)

        if len(list(temp_list)) <= 2:
            # print "无效商品名称"
            return

        else:
            # print "有效的商品名称"
            if list(temp_list)[-1] == '\n':
                # print "去掉换行之前--》"
                # print list(temp_list)
                # print "".join(list(temp_list))
                # print "去掉换行之后--》"
                changed =  temp_list.replace('\n','')
                # print changed
                new_str = "".join(changed)
                # print new_str
                # print new_str
                # print "测试插入的字符串是否格式正确"
                # print list(new_str)

            else :
                new_str = temp_list

        self.num_list.append(id)
        self.num_list.append(new_str)
        # print self.num_list
        # print type(self.num_list[0])
        # print type(self.num_list[1])
        #
        # print list(self.num_list[1])
        if self.num_list[0] == 10362511012 or self.num_list[0] == 10362424472 or  self.num_list[0]==10362488532:
            pass
        else:
            sql = "insert into muying_id_name values (%u,\"%s\");" % tuple(self.num_list)
            #没有重复的才加入数据库
            if self.isResist(self.num_list[0]) == 0:
                print sql
                ret = self.cursor.execute(sql)
                self.conn.commit()

                if ret == 0:
                    pass
                else:
                    self.conn.commit()
                  # print ret

    #负责关闭连接对象的游标
    def destr(self):

        self.cursor.close()
        self.conn.close()

    #判断该记录是否存在，存在返回1，不存在返回0
    def isResist(self,num):
        sql = "select * from muying_id_name where id = %u"%num
        re = self.cursor.execute(sql)
        # print num
        # print "是否存在================================"
        # print re
        if re == 0:
            print "不存在===================================="
            # print num
            return 0
        else:
            # print "已经存在==================================="
            return  1




if __name__ == "__main__":
    too = kang("muying_all_id_name.txt")
    too.read_file()
    too.destr()


