import datetime
import pymysql
import dbconfig


class DBHelper:

    def connect(self, database="crimemap"):
        print("Getting connection")
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def add_crime(self, category, date, latitude, longitude, desc):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (category, date, latitude, longitude, description) \
                     VALUES (%s, %s, %s, %s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(
                    query, (category, date, latitude, longitude, desc))
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

    def get_all_crimes(self):
        connection = self.connect()
        try:
            query = "SELECT latitude, longitude, date, category, description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            named_crimes = []
            for crime in cursor:
                named_crime = {
                    'latitude': crime[0],
                    'longitude': crime[1],
                    'date': datetime.datetime.strftime(crime[2], '%Y-%m-%d'),
                    'category': crime[3],
                    'description': crime[4]
                }
                named_crimes.append(named_crime)
            return named_crimes
        finally:
            connection.close()

