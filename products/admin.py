from django.contrib import admin

# Register your models here.
from .models import Category,Product,ProductImage,Newsletter,OrderItem,Order,Basket,ShippingInfo,BillingInfo,PaymentInfo,Wishlist,ProductRating,ProductComment

from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent",)
    search_fields = ("name",)

class  ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# class SkinTypeInline(admin.TabularInline):
#     model = SkinType.product.through  # many to many -de inline bele istifade olunur
#     extra = 0
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("id","title","price")
    inlines=[ImageInline]

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display=("id","name","parent")


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Newsletter)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Basket)
admin.site.register(ShippingInfo)
admin.site.register(BillingInfo)
admin.site.register(PaymentInfo)


admin.site.register(Wishlist)
admin.site.register(ProductComment)
admin.site.register(ProductRating)


