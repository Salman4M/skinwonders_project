from .models import Product,Category
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields=('title','name','status','skin')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','parent')