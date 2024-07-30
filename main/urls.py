from django.urls import path, include
from .views import home, products, category, post_view

urlpatterns = [

    path('', home),
    path('products', products),
    # category/25
    path('category/<int:category_id>', category, name='bolim'),
    path('post/<int:post_id>', post_view, name='post'),
]
