# coding=utf-8
import api.base_name as names
from route.BaseRoute import BaseRoute
from api.auth.registration_users import Registration


class RegistrationRoute(BaseRoute):
    """
    Роут регситрации
    """
    def __init__(self):
        super().__init__()
        self.login = None
        self.password = None
        self.name = None
        self.email = None
        self.arguments = [names.LOGIN, names.PASSWORD, names.NAME, names.EMAIL]
        for argument in self.arguments:
            self.parser.add_argument(argument)
        self.args = self.parser.parse_args()

    def parse_data(self):
        """
        Вычитываем данные
        """
        self.login = self.args.get(names.LOGIN, None)
        self.password = self.args.get(names.PASSWORD, None)
        self.name = self.args.get(names.NAME, None)
        self.email = self.args.get(names.EMAIL, None)

    def post(self):
        """
        Регистрация
        """
        self.parse_data()
        reg = Registration()
        uuid_user = reg.registration_user(self.login, self.password, self.name, self.email)
        return {names.UUID: uuid_user}, 200, names.HEADER
