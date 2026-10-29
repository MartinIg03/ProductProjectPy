from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            "product_id": "Product ID",
            "name": "Name",
            "stock_keep_unit": "Stock keep unit",
            "quantity": "Quantity",
            "price": "Price",
            "supplier": "Supplier",
        }

        widgets = {
            "product_id": forms.NumberInput(
                attrs={"placeholder": "e.g. 1", "class": "form-control"}
            ),
            "name": forms.TextInput(
                attrs={"placeholder": "e.g. shirt", "class": "form-control"}
            ),
            "stock_keep_unit": forms.TextInput(
                attrs={"placeholder": "e.g. S1234", "class": "form-control"}
            ),
            "quantity": forms.NumberInput(
                attrs={"placeholder": "e.g. 1", "class": "form-control"}
            ),
            "price": forms.NumberInput(
                attrs={"placeholder": "e.g. 14.99", "class": "form-control"}
            ),
            "supplier": forms.TextInput(
                attrs={"placeholder": "e.g. SUP-OOD", "class": "form-control"}
            ),
        }
