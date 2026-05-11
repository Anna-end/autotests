import pytest
from assertions.users_assertions import UsersAssertions
from models.user import UserPayload

class TestCreateAccount:

    @pytest.fixture(autouse=True)
    def setup(self, users):
        self.users = users

    def test_create_account_success(self):
        user = UserPayload()
        response = self.users.create_account(user.to_dict())
        UsersAssertions.assert_account_created(response)
        self.users.delete_account(user.email, user.password)  # teardown



class TestLogin:

    @pytest.fixture(autouse=True, scope="class")
    def test_user(self, users):
        user = UserPayload()
        users.create_account(user.to_dict())

        yield user

        users.delete_account(user.email, user.password)

    def test_valid_login(self, users, test_user):
        response = users.verify_login(test_user.email, test_user.password)
        UsersAssertions.assert_valid_login(response)

    def test_invalid_password(self, users, test_user):
        response = users.verify_login(test_user.email, "WRONG_PASSWORD")
        UsersAssertions.assert_invalid_password(response)

    def test_login_without_email(self, users, test_user):
        response = users.verify_login_without_email(test_user.password)
        UsersAssertions.assert_login_without_email(response)