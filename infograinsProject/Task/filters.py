import django_filters
from django_filters import DateFilter , CharFilter , ModelMultipleChoiceFilter

from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr="icontains")
    # category = ModelMultipleChoiceFilter(field_name='category',queryset = Product.objects.filter(product_owner__id = request.user))
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['category','product_owner']
