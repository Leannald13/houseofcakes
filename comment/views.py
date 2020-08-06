from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from comment.forms import CommentForm
from products.models import Product


def comment(request, product_id):

    post = get_object_or_404(Comment, pk=product_id)

    if request.method == 'POST':
        form = Comment(
            comment_body=request.POST['comment_body'],
            comment_user=request.user,
        )

        form.save()
        return render(request, 'products/product_detail.html')

    context = {
        'post': post,
        'form': CommentForm,
    }

    return render(request, 'products/product_detail.html', context)

