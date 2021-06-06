import django_filters
from django import forms

from core.widgets import PriceWidget
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "price": PriceWidget()
        }
        help_texts = {
            "price": "Must be <b>greater or equal to zero</b>."
        }


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ["name"]
