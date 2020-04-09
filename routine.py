import requests
import SECRETS, STATICS
import mysql.connector

def get(parameter_scope = None):
    global mydb
    ret = []

    try:
        mydb = mysql.connector.connect(
            host=SECRETS.mysqllogin.host,
            user=SECRETS.mysqllogin.user,
            passwd=SECRETS.mysqllogin.passwd,
            db = STATICS.mysqlnames.db
        )
        cursor = mydb.cursor()

        requestdata = {
            "grant_type":"client_credentials",
            "client_id":SECRETS.CLIENT_ID,
            "client_secret":SECRETS.CLIENT_SECRET
        }
        scopes = []

        if parameter_scope != None:
            scopes = []
            for ps in parameter_scope:
                scopes.append(ps)
        else:
            cursor.execute("SELECT scope FROM tb_token WHERE request;")
            mysqlresult = cursor.fetchall()
            for i in mysqlresult:
                scopes.append(i[0])
        for s in scopes:
            requestdata['scope'] = s #Name of the scope
            try: request = requests.post("https://api.toornament.com/oauth/v2/token", data = requestdata, timeout = 10)
            except Exception as err:
                ret.append({"error": True, "position": "scopes", "errortype": "code", "responsecode": 910, "scope": s})
                print(err)
                continue

            if request.status_code < 400:
                response = request.json()
                token = response.get("access_token")

                try:
                    cursor.execute("UPDATE tb_token SET token = '%s', timestamp = CURRENT_TIMESTAMP WHERE scope = '%s';" % (token, s))
                    mydb.commit()
                except mysql.connector.Error:
                    ret.append({"error": True, "errortype": "code", "position": "scopes", "responsecode": 951, "scope": s})
                except Exception:
                    ret.append({"error": True, "errortype": "code", "position": "scopes", "responsecode": 952, "scope": s})
                else:
                    ret.append({"error": False, "position": "scopes", "scope": s})
            else:
                ret.append({"error": True, "errortype": "code", "position": "scopes", "responsecode": request.status_code.__str__(), "scope": s})
    except mysql.connector.Error as err:
        ret.append({"error": True, "position": "mysqlglobal", "errortype": "code", "responsecode": 921})
    except Exception:
        ret.append({"error": True, "position": "mysqlglobal", "errortype": "code", "responsecode": 922})
    else:
        ret.append({"error": False, "position": "mysqlglobal"})
    finally:
        mydb.close()

    return ret
