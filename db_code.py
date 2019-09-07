import pymysql
import dbconfig

class DB:
    def connect(self, database = "crimemap"):
        return pymysql.connect(host="localhost",
                user=dbconfig.USER,
                passwd = dbconfig.PASSWORD,
                db = database)

    def insert_data(self, data):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO crimes (description) VALUES ('" + data + "')"
                cursor.execute(sql)
                connection.commit()
        finally:
            connection.close()

    def read_data(self):
        connection = self.connect();
        try:
            with connection.cursor() as cursor:
                sql = "SELECT description from crimes"
                cursor.execute(sql)
            return cursor.fetchall()

        finally:
            connection.close()

    def delete_data(self):
        connection = self.connect();
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM crimes"
                cursor.execute(sql)
                connection.commit()
        finally:
            connection.close()
