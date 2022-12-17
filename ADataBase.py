import sqlite3


class ADataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_products(self):
        sql = '''SELECT * FROM products'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Error reading DB")
        return []
