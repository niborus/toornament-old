# Abstract classes

from errors import *

class TestException(Exception):
    """Its a exception"""

from base_classes import abc
import request

# This is the connection to toornament, containing all tokens
class connection():

    def __init__(self, token: str):

        self.token = token

        self.test_connection() # Raises an error of login is failing

    def getTournament(self, tournament_id: int):

        r = request.prepare_tournament(token=self.token, id=tournament_id)

        r = r.execute()

        if r.status_code >= 400:
            raise TestException #@TODO Raise the correct exception with error information
        else:
            tournament = abc.tournament(r.json())

        return tournament

    def test_connection(self):
        """:raises LoginError if login fails"""

        r = request.prepare_tournaments(token=self.token, section="viewer")
        r = r.execute()

        if r.status_code >= 300:
            if r.status_code in [401, 403]:
                raise LoginError("Improper token has been passed.")
            else:
                raise LoginError("Couldn't login. Reciving response: {} from Toornament".format(r.status_code))