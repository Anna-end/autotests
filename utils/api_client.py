import requests

class ApiClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/x-www-form-urlencoded"})

    def _request(
                self,
                method: str,
                endpoint: str,
                **kwargs
        ) -> requests.Response:
            url = f"{self.base_url}{endpoint}"
            response = self.session.request(method, url, **kwargs)
            return response

    def get(
                self,
                endpoint: str,
                **kwargs
        ) -> requests.Response:
            return self._request("GET", endpoint, **kwargs)

    def post(
                self,
                endpoint: str,
                **kwargs
        ) -> requests.Response:
            return self._request("POST", endpoint, **kwargs)

    def put(
                self,
                endpoint: str,
                **kwargs
        ) -> requests.Response:
            return self._request("PUT", endpoint, **kwargs)

    def delete(
                self,
                endpoint: str,
                **kwargs,
        ) -> requests.Response:
            return self._request("DELETE", endpoint, **kwargs)

    def __enter__(self) -> "ApiClient":
            return self
    def __exit__(self, *args) -> None:
            self.session.close()