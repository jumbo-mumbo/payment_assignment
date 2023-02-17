from django.contrib import admin
from .models import Discount, Tax, Order, Item


admin.site.register([Discount, Tax])


@admin.register(Item)
class ItemAdminModel(admin.ModelAdmin):
    list_display = ["name", "price", "currency", "order"]

class ItemInline(admin.StackedInline):
    model = Item
    extra = 0
    

@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    list_display = ("order_id", "discount", "tax")
    fields = ("order_id", "discount", "tax")
    inlines = (ItemInline,)