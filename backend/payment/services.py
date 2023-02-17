import stripe


def perform_checkout_session(
    items, 
    coupon_percentage: float | None, 
    tax_percentage: float | None
    ):
    coupon_id = None
    tax_id = None
    client_url = "http://localhost:8080/"

    if coupon_percentage:
        stripe_coupon = stripe.Coupon.create(percent_off=coupon_percentage)
        coupon_id = stripe_coupon.get("id")
    
    if tax_percentage:
        tax_stripe = stripe.TaxRate.create(
                display_name="Order tax", 
                inclusive=False, 
                percentage=tax_percentage
                )
        tax_id = tax_stripe.get("id")
    
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=client_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=client_url + "cancelled",
            payment_method_types=['card'],
            mode='payment',
            discounts=[{"coupon": coupon_id}],
            line_items=[
                {
                    "quantity": 1,
                    "tax_rates": [tax_id] if tax_id else None,
                    "price_data":{
                        "currency": item.currency,
                        "unit_amount": int(item.price) * 100, 
                        "product_data": {
                            "name": item.name, 
                            "description": item.description
                            }
                        }
                } for item in items   
            ]
        )
        
        response = {"checkout_session_url": checkout_session.url}
        return response
        
    except Exception as e:
        response = {"error": e}
        print(response)
        return response

