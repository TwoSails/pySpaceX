class ApiNoSuccess(Exception):
    def __init__(self):
        self.message = "A 404 Error has occurred with the response from the API"

    def __str__(self):
        return self.message
