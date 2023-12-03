import django_filters
from services.choices import STATUS,SKINTYPE
from products.models import Product

class ProductFilter(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='total_price')
    status= django_filters.ChoiceFilter(choices=STATUS)
    skin = django_filters.ChoiceFilter(choices = SKINTYPE )
    name = django_filters.CharFilter(lookup_expr="icontains")
 
    class Meta:
        model=Product
        fields=("name", "price_range","status","skin")

