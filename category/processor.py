from category.models import Category

def show_cat(request):
    return {'cats': Category.objects.filter()}