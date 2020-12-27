import pymysql
import xlrd
import datetime

database = pymysql.connect("127.0.0.1", "test", "test", "db", charset='utf8')
cursor = database.cursor()

sql1 = "DELETE FROM data ;"
cursor.execute(sql1)
database.commit()


def change_date(date_excel):
    first_date = datetime.date(1899, 12, 31).toordinal() - 1
    if isinstance(date_excel, float):
        date_excel = int(date_excel)
    date_mysql = datetime.date.fromordinal(first_date + date_excel)
    return date_mysql.strftime("%Y-%m-%d")


xlsx = xlrd.open_workbook('d:/7月下旬入库表.xlsx')
table = xlsx.sheet_by_index(0)
for i in range(1, table.nrows):
    sql2 = "INSERT INTO data (date,company,province,price,weight) VALUES ('%s','%s','%s','%s','%s');" % (
    change_date(table.cell_value(i, 0)), table.cell_value(i, 1), table.cell_value(i, 2), table.cell_value(i, 3),table.cell_value(i, 4))
    cursor.execute(sql2)
    database.commit()


sql3 ="SELECT SUM(weight) FROM data WHERE date>'2018-07-21' AND date<'2018-07-25' AND company='王五小麦' AND province='河北' "
cursor.execute(sql3)
print(cursor.fetchall()[0][0])

database.close()
