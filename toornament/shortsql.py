import mysql.connector
import STATICS, SECRETS

def select(command):
    try:
        mydb = mysql.connector.connect(
            host=SECRETS.mysqllogin.host,
            user=SECRETS.mysqllogin.user,
            passwd=SECRETS.mysqllogin.passwd,
            db=STATICS.mysqlnames.db,
        )
        cursor = mydb.cursor()
        cursor.execute(command)
        sqlresult = cursor.fetchall()
    except Exception as err:
        print(err)
        return {"error": True, "errortype": "code", "responsecode": 922}
    finally:
        try:
            mydb.close()
        except:
            pass

    return {"error": False, "result": sqlresult}

def write(command):
    try:
        mydb = mysql.connector.connect(
            host=SECRETS.mysqllogin.host,
            user=SECRETS.mysqllogin.user,
            passwd=SECRETS.mysqllogin.passwd,
            db=STATICS.mysqlnames.db,
        )
        cursor = mydb.cursor()
        cursor.execute(command)
        mydb.commit()

        rows = cursor.rowcount

    except Exception as err:
        print(command)
        print(err)
        return {"error": True, "errortype": "code", "responsecode": 922}
    finally:
        try:
            mydb.close()
        except:
            pass

    return {"error": False, "row": rows}
