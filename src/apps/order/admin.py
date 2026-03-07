from django.contrib import admin
from apps.order.models import Cart, Order, OrderItem

# Register your models here.

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)


