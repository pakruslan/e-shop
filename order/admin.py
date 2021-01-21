from django.contrib import admin


from .models import Order, OrderItem


class OrderItemsInline(admin.TabularInline):
    model = Order.item.through
    fields = ['product', 'quantity', 'price']
    readonly_fields = ['product', 'quantity', 'price']
    extra = 0 

    def product(self, instance):
        return instance.order_items
    
    def quantity(self, instance):
        return instance.order_items.quantity

    
    def price(self, instance):
        return instance.order_items.price



class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]
    exclude = ['item']
    list_display = (
        'id', 'user', 'status', 'created_at', 'total'
    )



admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)