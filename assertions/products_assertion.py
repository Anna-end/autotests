from requests import Response

class ProductAssertion:

    @staticmethod
    def assert_successful_product_list(response: Response) -> None:
        assert response.json()["responseCode"] == 200
        products = response.json()['products']
        assert len(products) > 0

    @staticmethod
    def assert_invalid_post_product_list(response: Response) -> None:
        assert response.json()["responseCode"] == 405
        assert response.json()["message"] == "This request method is not supported."

    @staticmethod
    def assert_successful_search_products(response: Response) -> None:
        assert response.json()["responseCode"] == 200
        products = response.json()['products']
        assert len(products) > 0