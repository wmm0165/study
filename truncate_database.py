import pymysql


def execude_sql(sql):
    con = pymysql.connect('10.1.1.71', 'root', 'root123', 'test', charset='utf8')
    cur = con.cursor()
    cur.execute(sql)
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()


sql = """select CONCAT('truncate table ',  table_name, ';')  from information_schema.`TABLES` where TABLE_SCHEMA='test'"""

print(sql)
execude_sql(sql)

