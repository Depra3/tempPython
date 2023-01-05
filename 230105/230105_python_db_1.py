import pymysql

def get_connection():
    conn = pymysql.connect(host='127.0.0.1',user='root',password='1234',charset='utf8')
    return conn

def get_student_list(stu_name):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = 'select stu_idx, stu_name, stu_age, stu_addr from student_table;'

    if stu_name != None and len(stu_name) > 0:
        sql = sql + 'where stu_name like {}'
        # sql += 'where stu_name like {}'
    
    if stu_name != None and len(stu_name) > 0:
        cursor.execute(sql.format(stu_name))
    else:
        cursor.execute(sql)
    
    result = cursor.fetchall()

    temp_list = []
    for row in result:
        temp_dic = {}
        temp_dic['stu_idx'] = row[0]
        temp_dic['stu_name'] = row[1]
        temp_dic['stu_age'] = row[2]
        temp_dic['stu_addr'] = row[3]

        temp_list.append(temp_dic)

        return temp_list