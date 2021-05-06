from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.

# class ItemAdmin(admin.ModelAdmin):
#     readonly_fields = ('user','price',)
#     # def get_readonly_display(self, request, obj=None):
#     #     if obj:
#     #         return ['price','user']
#     #     else:
#     #         return []


admin.site.register(Cart)
admin.site.register(CartItem)
