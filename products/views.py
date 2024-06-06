from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import SearchForm
from .models import CategoryModel, ProductModel


# def home_page(request):
#
#     categories = CategoryModel.objects.all()
#     products = ProductModel.objects.all()
#     # print -> Laptops,smart,pencil
#     context = {'categories': categories, 'products': products}
#     return render(request, template_name='index.html', context=context)

class HomePage(ListView):
    template_name = 'index.html'
    model = ProductModel
    context_object_name = 'products'
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        return context


def search(request):
    # search=='Iphone12'
    if request.method == 'POST':
        # <input name='search_product'> <button>
        get_product = request.POST.get('search_product')
        #search_product=Iphone12 Iphone13
        try:
            exact_product = ProductModel.objects.get(title__icontains=get_product)
            return redirect(f'/products/{exact_product.id}')
        except:
            return redirect('/')


# Iphone12 -> Iphone12,price,
def product_page(request, id):
    product = ProductModel.objects.get(id=id)
    context = {'product': product}
    return render(request, template_name='single-product.html',
                  context=context)
