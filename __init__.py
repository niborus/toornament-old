# Abstract classes
from abc import abc
import request

# This is the connection to toornament, containing all tokens
class connection():

    def __init__(self, token: str):

        self.token = token

    def getTournament(self, tournament_id: int):

        return abc.tournament(request.prepare_tournament(token=self.token))