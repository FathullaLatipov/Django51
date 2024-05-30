from django.shortcuts import render

from .models import CategoryModel, ProductModel


def home_page(request):

    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    # print -> Laptops,smart,pencil
    context = {'categories': categories, 'products': products}
    return render(request, template_name='index.html', context=context)

