# 900er-Fehler
# 901 - Missing Variable
# 910 - Problem with the Internet-Connection

import requests
import SECRETS, shortsql
import shortsql

# Class will prepare an request. Instance can be altered.
class prep_request():

    def __init__(self, token="", host ="https://api.toornament.com", section ="viewer", timeout = 7):
        self.token = token
        self.host = host
        self.section = section
        self.timeout = timeout
        self.range = None

    def url_path(self):
        return ""

    def add_head(self):
        return {}

    def create_url(self):

        url_var = {
            "host": self.host,
            "section": self.section,
            "path": self.url_path()
        }

        url = "{host}/{section}/v2{path}".format(**url_var)

        return url

    def execute(self):
        request_head = {
            "X-Api-Key": self.token,
        }

        request_head.update(self.add_head())

        request_query = {}

        data = {}

        request = requests.get(self.create_url(), headers=request_head, params=request_query,
                               json=data, timeout=7)

        return request

class prepare_tournaments(prep_request):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.range = {
            "name": "tournaments",
            "start": 0,
            "end": 0
        }

    def url_path(self):
        return "/tournaments/featured"

    def range_string(self):
        return "{name}={start}-{end}".format(**self.range)

    def add_head(self):
        return {"Range": self.range_string()}


class prepare_tournament(prep_request):

    def __init__(self, id=None, **kwargs):
        super().__init__(**kwargs)
        self.id = id

    def url_path(self):
        return "/tournaments/{}".format(self.id)  # @ToDo Die requests noch Testen


def get(type_of_request, tournament_id, scope=None, path="", sub_id=None, range_from=0, range_until=49, data=None,
        request_query=None):  # type_of_request can be 'single', 'list', 'post' or 'patch'

    if data is None:
        data = {}
    if request_query is None:
        request_query = {}

    global mydb

    request_head = {
        "X-Api-Key": SECRETS.TOORNAMENT_TOKEN,
    }

    if type_of_request == 'list':
        request_head["Range"] = "%s=%d-%d" % (path, range_from, range_until)

    if scope != None:
        sqlresult = shortsql.select("SELECT * FROM tb_token WHERE scope = '%s';" % (scope))
        if sqlresult.get("error", True):
            return sqlresult
        else:
            sqlresult = sqlresult.get("result", [])

        if sqlresult != []:
            auth_token = sqlresult[0][1]
            request_head["Authorization"] = "Bearer " + auth_token
            api_link = "organizer"
        else:
            return {"error": True, "errortype": "code", "responsecode": 901}

    else:
        api_link = "viewer"

    try:
        if path != "":
            path = "/" + path

        requested_url = "https://api.toornament.com/%s/v2/tournaments/%s%s" % (api_link, str(tournament_id), path)
        if not sub_id is None:
            requested_url += "/" + sub_id.__str__()

        list_of_request = {
            "single": requests.get,
            "list": requests.get,
            "get": requests.get,
            "post": requests.post,
            "patch": requests.patch,
            "delete": requests.delete
        }

        request = list_of_request.get(type_of_request)(requested_url, headers=request_head, params=request_query,
                                                       json=data, timeout=7)

    except Exception as err:
        print("Fehler in der API (get): " + str(err))
        return {"error": True, "errortype": "code", "responsecode": 910}

    if request.status_code < 400 and type_of_request == "delete":
        return {"error": False, "responsecode": request.status_code}
    elif request.status_code < 400:
        return {"error": False, "data": request.json(), "responsecode": request.status_code, "head": request.headers}
    else:
        print(str(request.status_code) + "Fehler beim Abrufen der URL (api.get):" + str(request.url))
        if request.status_code == 400:
            print(request.text)
        return {"error": True, "errortype": "code", "responsecode": request.status_code, "response": request.text}


def getall(tournament_id, scope=None, path=""):
    try:
        api_data = get("list", tournament_id, scope, path=path, range_from=0, range_until=0)
        Range = int(api_data.get("head", {}).get("Content-Range", "0-0/0").split("/")[1])
        all_participant = []

        count = 0
        while count <= (Range // 50):
            range_from = 50 * count
            range_until = 50 * count + 49
            api_data = get("list", tournament_id, scope, path=path, range_from=range_from,
                           range_until=range_until)

            if api_data.get("error", True):
                return api_data

            all_participant.extend(api_data.get("data", []))
            count += 1

        return {"error": False, "data": all_participant}

    except Exception as err:
        print(err)
        return {"error": True, "errortype": "code", "responsecode": 911}


def getnextmatches(toornament_id, participant_id, organizer=False):
    query = {
        "participant_ids": [participant_id],
        "statuses": "pending"
    }
    if organizer:
        scope = "organizer:result"
    else:
        scope = None
    api_return = get("list", toornament_id, scope=scope, path="matches", range_from=0, range_until=0,
                     request_query=query)

    return api_return
