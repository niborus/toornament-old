import mysql.connector
import SECRETS, STATICS
from toornament.scopes import scopes

def init():

    try:
        mydb = mysql.connector.connect(
            host=SECRETS.mysqllogin.host,
            user=SECRETS.mysqllogin.user,
            passwd=SECRETS.mysqllogin.passwd,
        )
        mydb.close()
    except mysql.connector.Error as err:
        print("Something went wrong while connecting: {}".format(err))
    else:
        try:
            mydb = mysql.connector.connect(
                host=SECRETS.mysqllogin.host,
                user=SECRETS.mysqllogin.user,
                passwd=SECRETS.mysqllogin.passwd,
            )
            cursor = mydb.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS %s;" % STATICS.mysqlnames.db)
            cursor.execute("USE %s;" % STATICS.mysqlnames.db)
            cursor.execute("""CREATE TABLE IF NOT EXISTS tb_token(
                                scope VARCHAR(33) PRIMARY KEY,
                                token VARCHAR(1024),
                                request BOOLEAN,
                                timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                                );""")

            for scope in scopes:
                cursor.execute("SELECT * FROM tb_token WHERE scope = '%s';" % scope[0])
                mysqlresult = cursor.fetchall()

                if len(mysqlresult) == 0:
                    try:
                        cursor.execute("INSERT INTO tb_token (scope, request) VALUES ('%s', %s);" % (scope[0], str(scope[1])))
                        mydb.commit()
                    except:
                        print("Can't add scope %s" % scope[0])
                    else:
                        print("Added scope %s" % scope[0])

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        except Exception as Ex:
            print("Something went wrong " + Ex.__str__())
        finally:
            mydb.close()

init()
