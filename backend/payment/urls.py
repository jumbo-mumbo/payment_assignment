from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ItemViewSet,
    #ItemApiView, 
    OrderApiView, 
    get_public_key, 
    payment)

router = DefaultRouter()
router.register(r'shop/item', ItemViewSet, basename="item")


urlpatterns = [
    #path("shop/item/<int:id>", ItemApiView.as_view(), name="item"),
    path("shop/order/<str:order_id>", OrderApiView.as_view(), name="order"),
    path("create_checkout_session", payment, name="payment"),
    path("get_public_key", get_public_key, name="public key"),
    #path("buy/{id:int}")

] + router.urls