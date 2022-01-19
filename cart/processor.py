from cart.sessions import Cart

def show_cart(request):
    cart = Cart(request)
    return {'cart_count': cart.count_cart}