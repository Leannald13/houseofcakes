from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    readonly_fields = ('date', 'delivery_cost', 'order_total', 'grand_total')

admin.site.register(Order, OrderAdmin)
