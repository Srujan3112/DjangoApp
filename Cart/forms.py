from django.forms import ModelForm, HiddenInput
from .models import CartItem
from django import forms
from Base.models import Product


class CartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CartItemForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['user'].widget = HiddenInput()
            self.fields['product'].widget = HiddenInput()
            self.fields['price'].widget = HiddenInput()
            self.fields['ordered'].widget = HiddenInput()
            self.fields['cart'].widget = HiddenInput()

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['product']
        if quantity > product.quantity:
            raise forms.ValidationError(f"Requested quantity is not available , Only {quantity} are available")
        return quantity
