import pytest
from payment.models import Item


@pytest.mark.django_db
def test_item_create():
    item = Item(currency='usd', name='test_name', price=1000)
    item.save()
    assert Item.objects.count() == 1


