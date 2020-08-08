from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('<product_id>', views.comment, name='comment'),
]
