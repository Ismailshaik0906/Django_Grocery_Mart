from .models import Category


def add_categories_to_context(request):
    categories = Category.objects.all()
    return {'categories': categories}


