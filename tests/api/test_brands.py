import pytest
from assertions.brands_assertion import BrandsAssertion

class TestBrands:
    @pytest.fixture(autouse=True)
    def setup(self, brands):
        self.brands = brands

    def test_get_all_brands(self):
        response = self.brands.get_all_brands()
        BrandsAssertion.assert_successful_brands_list(response)

    def test_invalid_put_to_brand_list(self):
        response = self.brands.put_to_brand_list()
        BrandsAssertion.assert_invalid_put_to_brand_list(response)