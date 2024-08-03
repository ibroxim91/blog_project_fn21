from django.urls import path, include
from .views import home, products, category, post_view, post_reactions

app_name = 'main'

urlpatterns = [

    path('', home),
    path('products', products),
    path('category/<int:category_id>', category, name='category'),
    path('post/<int:post_id>', post_view, name='post'),
    path('post/<int:post_id>/reactions', post_reactions, name='post_reactions'),
]
