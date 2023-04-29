import pytest
from rest_framework.test import APIClient
from payment.models import Item


@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def item_payload():
    payload = {
        'currency': 'usd',
        'name': 'TestName',
        'price': 1000
    }

    return payload

@pytest.fixture
def create_item():
    item = Item(currency='usd', name='TestName', price=1000)
    item.save()
    return item