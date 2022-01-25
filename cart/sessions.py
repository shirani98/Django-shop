from decimal import Decimal
from shop.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, product , quantity):
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0 , 'price' : str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def save(self):
        self.session.modified = True
        
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']= product
        for item in cart.values():
            item['total_price'] = item['quantity'] * Decimal(item['price'])
            yield item
        
    def get_total_price(self):
        return sum(Decimal(item['price'])* item['quantity'] for item in self.cart.values())
     
    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] > 1:
                self.cart[product_id]['quantity'] -= 1
                self.save()
            else:
                del self.cart[product_id]
                self.save()
    
    def count_cart(self):
        return len(self.cart)
    
    def clean(self):
        del self.session['cart']
        self.save()
        
        
        
               