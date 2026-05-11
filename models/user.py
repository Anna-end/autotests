from dataclasses import dataclass, field
from utils.data_generator import random_email, random_phone

@dataclass
class UserPayload:
    email: str = field(default_factory=random_email)
    mobile_number: str = field(default_factory=random_phone)
    name: str = "Test User"
    password: str = "Test@12345"
    title: str = "Mr"
    birth_date: str = "15"
    birth_month: str = "June"
    birth_year: str = "1990"
    firstname: str = "Test"
    lastname: str = "User"
    company: str = "QA Corp"
    address1: str = "123 Test Street"
    address2: str = "Suite 456"
    country: str = "United States"
    zipcode: str = "10001"
    state: str = "New York"
    city: str = "New York"

    def to_dict(self) -> dict:
        return self.__dict__