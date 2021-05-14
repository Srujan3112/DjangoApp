from django import template
from Cart.models import CartItem, Cart
from Base.models import Product

register = template.Library()


@register.simple_tag
def is_ordered(request, product):
    try:
        cart_item = CartItem.objects.get(product=product.id, user=request.user)
    except:
        return None

    return cart_item.ordered


@register.simple_tag
def return_product(request, id_val):
    try:
        product = Product.objects.get(id=id_val)
    except:
        return None
    return product
