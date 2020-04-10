class Error(Exception):
    pass

class LoginError(Error):
    def __init__(self, message):

        self.message = message