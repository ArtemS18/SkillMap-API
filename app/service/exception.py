class ServiceExeption(Exception):
    ...

class NotFoundError(ServiceExeption):
    def __init__(self, name: str):
        self.name = name

class AlreadyExist(ServiceExeption):
    def __init__(self, name: str):
        self.name = name

class BadRequest(ServiceExeption):
    ...

class BadCredentials(ServiceExeption):
    ...

class BadJWTCredentials(ServiceExeption):
    ...