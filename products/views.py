from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product
from comment.models import Comment
from comment.forms import CommentForm

# Create your views here.


def all_products(request):
    """A view to show each product item and description
       allows user to search cakes """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    comment = Comment.objects.filter(product_id=product_id)

    context = {
        'product': product,
        'form': CommentForm,
        'comment': comment,
    }

    return render(request, 'products/product_detail.html', context)
