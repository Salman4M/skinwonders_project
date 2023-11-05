import django_filters
from services.choices import STATUS
from products.models import SkinType,Product

class ProductFilter(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='total_price')
    status= django_filters.ChoiceFilter(choices=STATUS)
    skintype = django_filters.ModelChoiceFilter(queryset=SkinType.objects.all())
    name = django_filters.CharFilter(lookup_expr="icontains")
 
    class Meta:
        model=Product
        fields=("price_range","status","skintype")
