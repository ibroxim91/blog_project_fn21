from django.urls import path, include
from .views import home, products, category, post_view

app_name = 'main'

urlpatterns = [

    path('', home),
    path('products', products),
    path('category/<int:category_id>', category, name='category'),
    path('post/<int:post_id>', post_view, name='post'),
]
