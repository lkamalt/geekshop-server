from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    """ Форма для работы с авторизацией пользователя """

    class Meta:
        model = User
        fileds = ('username', 'password')
