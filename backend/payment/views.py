from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Item, Order
from .services import perform_checkout_session
from .serializers import ItemSerializer, OrderSerialiser

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemApiView(APIView):
    def get(self, request, id: int):
        try:
            item = Item.objects.get(id=id)
            currency_region = item.get_currency_display()
            item_serializer = ItemSerializer(item)
            
            data = item_serializer.data
            data["region"] = currency_region

            return Response(
                data=data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND)

    
class OrderApiView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(order_id=order_id)
            items = order.items.all()
            order_serializer = OrderSerialiser(order)

            data = order_serializer.data
            data["items"] = [ItemSerializer(item).data for item in items]


            return Response(
                data=data, status=status.HTTP_200_OK
                )
            
        except ObjectDoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        

@api_view(["GET"])
def payment(request: Request):
    coupon = None
    tax = None

    if "id" in request.query_params:
        item_id = request.query_params.get("id")
        items = [Item.objects.get(id=item_id)]
    
    else: # if "order_id" in query
        order_id = request.query_params.get("order_id")
        order = Order.objects.get(order_id=order_id)
        items = order.items.all()
        
        coupon = float(order.discount.percent) if order.discount else None
        tax = float(order.tax.percent) if order.tax else None
            
    checkout_session_url = perform_checkout_session(
        items=items, 
        coupon_percentage=coupon,
        tax_percentage=tax
        )
    return Response(
            data=checkout_session_url,
            status=status.HTTP_200_OK)


@api_view(["GET"])
def get_public_key(request: Request):
    stripe_config = {"publicKey": settings.STRIPE_PUBLIC_KEY}
    return Response(data=stripe_config, status=status.HTTP_200_OK)

