import pytest
from .conftest import api_client, item_payload, create_item

from rest_framework.test import APIClient
from rest_framework import status, reverse

from payment.models import Item
from payment.serializers import ItemSerializer


@pytest.mark.django_db
def test_create_item_api(api_client, item_payload):
    url = '/api/shop/item/'
    response = api_client.post(url, item_payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Item.objects.count() == 1


@pytest.mark.django_db
def test_get_item_api(api_client, create_item):
    url = '/api/shop/item/'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    item_data = dict(response.data[0])
    item = ItemSerializer(create_item).data
    
    item_data['order'] = "None"
    item['order'] = "None"

    assert item_data == item

