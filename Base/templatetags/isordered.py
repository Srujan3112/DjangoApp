from django import template
from Cart.models import CartItem, Cart

register = template.Library()


@register.simple_tag
def is_ordered(request, product):
    try:
        cart_item = CartItem.objects.get(product=product.id, user=request.user)
    except:
        return None

    return cart_item.ordered
