from shop.models import Product
class Visited ():
    def __init__(self, request):
        self.session = request.session
        visited = self.session.get('visited')
        if not visited:
            visited = self.session['visited'] = {}
        self.visited = visited
        
    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.visited:
            self.visited[product_id] = {'product_id': product.id }
        self.save()
        
    def save(self):
        if len(self.visited) >  4:
            for item in self.visited :
                del self.visited[item]
                break
        self.session.modified = True
        
    def __iter__(self):
        product_ids = self.visited.keys()
        products = Product.objects.filter(id__in = product_ids)
        for product in products:
            yield product
                    