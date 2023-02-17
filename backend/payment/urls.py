from django.urls import path
from .views import (
    ItemApiView, 
    OrderApiView, 
    get_public_key, 
    payment)


urlpatterns = [
    path("shop/item/<int:id>", ItemApiView.as_view(), name="item"),
    path("shop/order/<str:order_id>", OrderApiView.as_view(), name="order"),
    path("create_checkout_session", payment, name="payment"),
    path("get_public_key", get_public_key, name="public key"),
    
    #path("buy/{id:int}")
]