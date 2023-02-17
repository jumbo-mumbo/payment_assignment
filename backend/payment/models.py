from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings

import uuid


class BasePercentModel(models.Model):
    class Meta:
        abstract = True
        
    percent = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(100)], help_text="Процент"
    )

    def __str__(self) -> str:
        return f"{self.percent}%"

    
class Tax(BasePercentModel):
    pass


class Discount(BasePercentModel):
    pass


class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4)
    tax = models.ForeignKey(
        Tax, 
        on_delete=models.CASCADE, 
        help_text="Процент налога", 
        blank=True, 
        null=True
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        help_text="Процент скидки",
        blank=True,
        null=True,
    )

    @property
    def items_name(self):
        names = [item.name for item in self.items.all()]
        return names

    @property
    def items_price(self):
        price_list = [item.price for item in self.items.all()]
        return price_list

    @property
    def order_price(self):
        items_sum = sum(self.items_price)
        discount = self.discount.percent
        tax = self.tax.percent

        if self.discount:
            items_sum -= items_sum * (discount / 100)  # Calculate discount

        if self.tax:
            items_sum += items_sum * (tax / 100)  # Calculate tax

        return items_sum  # sum with discount and tax

    def __str__(self) -> str:
        return f"{self.order_id}"


class Item(models.Model):  
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    currency = models.CharField(
        max_length=3, choices=settings.CURRENCIES, default=("usd", "United States")
        )
    order = models.ForeignKey(
        Order, 
        related_name="items", 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )
    name = models.CharField(
        max_length=256,
        verbose_name="Name",
    )
    description = models.TextField(
        max_length=1024, verbose_name="Description", blank=True, default="No description"
    )
    price = models.PositiveIntegerField(verbose_name="Price")

    
    def __str__(self) -> str:
        return f"{self.name}"

