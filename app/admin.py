from django.contrib import admin
from .models import Table, Order, OrderItem, MenuItem, Category

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display =['number']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['peple_count']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display =['count']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display =('name','description', 'price')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['cat_name']

# admin.site.register(Table)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(Category)
# admin.site.register(MenuItem)
