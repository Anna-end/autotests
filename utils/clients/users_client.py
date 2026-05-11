from datetime import date


class UsersClient:
    def __init__(self, client):
        self._client = client

    def verify_login(self, email: str, password: str):
        return self._client.post("/api/verifyLogin" , data={"email": email, "password": password})

    def verify_login_without_email(self, password: str):
        return self._client.post("/api/verifyLogin", data={"password": password})

    def delete_verify_login(self):
        return self._client.delete("/api/verifyLogin")

    def create_account(self, payload: dict):
        return self._client.post("/api/createAccount", data=payload)

    def delete_account(self, email: str, password: str):
        return self._client.delete("/api/deleteAccount", data={"email": email, "password": password})

    def update_account(self, payload: dict):
        return self._client.put("/api/updateAccount", data=payload)

    def get_user_by_email(self, email: str):
        return self._client.get("/api/getUserDetailByEmail", params={"email": email})