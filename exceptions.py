class BaseError(Exception):
    def __init__(self, status_code, message, error):
        self.status_code = status_code
        self.message = message
        self.error = error

    def to_response(self):
        return {
                   "error": self.error,
                   "message": self.message
               }, self.status_code
