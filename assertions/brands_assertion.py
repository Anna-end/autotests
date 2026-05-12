from requests import Response

class BrandsAssertion:

    @staticmethod
    def assert_successful_brands_list(response: Response) -> None:
        assert response.json()["responseCode"] == 200
        products = response.json()['brands']
        assert len(products) > 0

    @staticmethod
    def assert_invalid_put_to_brand_list(response: Response) -> None:
        assert response.json()["responseCode"] == 405
        assert response.json()["message"] == "This request method is not supported."