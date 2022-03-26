from basket.models import Basket


def show_cart(request):
    if request.COOKIES.get('basket_id'):
        basket = Basket.objects.get(id=request.COOKIES.get('basket_id'))
        return {'cart_count': basket.basket_inline.count()}
    else:
        return {'cart_count': 0}
