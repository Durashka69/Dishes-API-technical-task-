from base_config import *

from apps.users.models import User


def create_test_users():
    emails = (
        'example@gmail.com',
        'test@gmail.com',
        'user@gmail.com'
    )

    User.objects.create_superuser(email='admin@gmail.com', password='admin')

    for email in emails:
        User.objects.create_user(email=email, password="password")


if __name__ == "__main__":
    create_test_users()
