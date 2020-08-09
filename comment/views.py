from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Comment
from comment.forms import CommentForm
from products.models import Product


@login_required()
def comment(request, product_id):

    if request.method == 'POST':

        form = Comment(
            comment_body=request.POST['comment_body'],
            comment_user=request.user,
            Product=product_id,

        )

        form.save()

    else:

        comment = get_object_or_404(Comment, pk=product_id)

        form = Comment(
            comment_body=request.GET['comment_body'],
            comment_user=request.GET['user'],
            Product=request.GET['product_id'],
        )

        form.save()

        context = {
                'form': CommentForm,
            }
 
        return redirect(reverse('product_detail', kwargs={'product_id': product_id}), context)
