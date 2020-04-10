# Abstract classes

from base_classes import abc
import request

# This is the connection to toornament, containing all tokens
class connection():

    def __init__(self, token: str):

        self.token = token

    def getTournament(self, tournament_id: int):

        r = request.prepare_tournament(token=self.token, id=tournament_id)

        r = r.execute()

        if r.status_code >= 400:
            raise Exception #@TODO Raise the correct exception with error information
        else:
            tournament = abc.tournament(r.json())

        return tournament