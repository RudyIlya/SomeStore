from .cart import Cart


def cart(request):
    cart = Cart(request)
    return {
        'cart': cart,
        'cart_product_ids': cart.get_products_ids(),
        }