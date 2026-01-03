class ServiceExeption(Exception): ...


class NotFoundError(ServiceExeption):
    def __init__(self, name: str):
        self.name = name


class AlreadyExist(ServiceExeption):
    def __init__(self, name: str):
        self.name = name


class BadRequest(ServiceExeption):
    def __init__(self, detail: str | None = None):
        self.detail = detail


class BadCredentials(ServiceExeption): ...


class BadJWTCredentials(ServiceExeption): ...
