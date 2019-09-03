import pymysql
import dbconfig

connection = pymysql.connect(host='localhost', user=dbconfig.USER, passwd = dbconfig.PASSWORD)

try:
    with connection.cursor() as cursor:
        sql =  "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
        id int NOT NULL AUTO_INCREMENT,
        latitude float(10,6),
        longitude float(10,6),
        date DATETIME,
        category VARCHAR(50),
        description VARCHAR(1000),
        updated_at timestamp,
        primary key (id)
        )"""
        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()
