import pytest
from assertions.products_assertion import ProductAssertion


class TestProductClient:
    @pytest.fixture(autouse=True)
    def setup(self, product):
        self.product = product
        self._search_payload = {"search_product": "top"}

    def test_get_all_products(self):
        response = self.product.get_all_products()
        ProductAssertion.assert_successful_product_list(response)

    def test_post_to_product_list(self):
        response = self.product.post_to_product_list()
        ProductAssertion.assert_invalid_post_product_list(response)

    def test_search_products(self):
        response = self.product.search_products(self._search_payload)
        ProductAssertion.assert_successful_search_products(response)