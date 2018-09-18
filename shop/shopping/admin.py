from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Item,Order

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','amount','photo_tag']

    def photo_tag(self,item): # 상품 미리보기 구현
        if item.photo:
            return mark_safe('<img src="{}"/>'.format(item.photo.url))
        return None

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['merchant_uid', 'name', 'status']