class AppException(Exception):
    @property
    def message(self) -> str:
        return "Something went wrong"


class UnexpectedError(AppException):
    pass
