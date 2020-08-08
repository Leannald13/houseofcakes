from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Comment
from comment.forms import CommentForm
from products.models import Product

def comment(request, product_id):

    comment = get_object_or_404(Comment, pk=product_id)

    if request.method == 'POST':

        form = Comment(
            comment_body=request.POST['comment_body'],
            comment_user=request.user,
            Product=product_id,

        )

        form.save()

        context = {
            'form': CommentForm,
         }

        return redirect(reverse('product_detail', kwargs={'product_id': product_id}))
