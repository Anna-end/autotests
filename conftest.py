import pytest
from utils.api_client import ApiClient
from utils.clients.product_client import ProductClient
from utils.clients.brands_client import BrandsClient
from utils.clients.users_client import UsersClient
from settings import API_URL

@pytest.fixture(scope="session")
def api_base_url():
    return API_URL

@pytest.fixture(scope="session")
def http_client(api_base_url):
    with ApiClient(api_base_url) as client:
        yield client

@pytest.fixture(scope="session")
def product(http_client):
    return ProductClient(http_client)

@pytest.fixture(scope="session")
def users(http_client):
    return UsersClient(http_client)

@pytest.fixture(scope="session")
def brands(http_client):
    return BrandsClient(http_client)