from django.shortcuts import render, redirect, reverse, get_object_or_404
import django.contrib import messages
from .models import Product
# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    # Returns all products from DB

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

    context = {
        'products': products,
    }
    # Products will now be available in templates
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    # Products will now be available in templates
    return render(request, 'products/product_detail.html', context)
