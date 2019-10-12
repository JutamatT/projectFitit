from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def redy(self):
        import users.singals
