import flask_login

from .. import login_manager

# TODO: Replace with method in user to check any database
users = {'test@temp.com': {'password': 'pass'}}


# TODO: Flesh out user model
class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user
