from requests import Response

class UsersAssertions:
    @staticmethod
    def assert_valid_login(response: Response) -> None:
        assert response.status_code == 200
        assert response.json()["message"] == "User exists!"

    @staticmethod
    def assert_account_created(response: Response) -> None:
        assert response.status_code == 200
        assert response.json()["message"] == "User created!"

    @staticmethod
    def assert_invalid_password(response: Response) -> None:
        assert response.json()["responseCode"] == 404
        assert response.json()["message"] == "User not found!"

    @staticmethod
    def assert_login_without_email(response: Response) -> None:
        assert response.json()["responseCode"] == 400
        assert response.json()["message"] == "Bad request, email or password parameter is missing in POST request."