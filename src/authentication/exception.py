from core.exception import BaseCustomException


class UserException:
    UserAlreadyExistsException = BaseCustomException(code=400, detail='User already exists')
    UserNotFoundException = BaseCustomException(code=400, detail='User not found')