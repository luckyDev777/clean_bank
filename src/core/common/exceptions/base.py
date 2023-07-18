class AppException(Exception):
    @property
    def message(self) -> str:
        return f"Something went wrong"


class UnexpectedError(AppException):
    pass
