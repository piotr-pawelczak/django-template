import pytest

from {{ cookiecutter.project_slug }}.users.models import User


@pytest.mark.django_db
class TestUserManager:
    def test_create_user(self):
        user = User.objects.create_user(email="example@test.com", password="test")
        assert user.email == "example@test.com"
