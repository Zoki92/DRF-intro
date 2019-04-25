from django.urls import path
from . import views


urlpatterns = [
    path('products/<int:pk>/reviews/<int:review_id>',
         views.ReviewDetail.as_view(),
         name='review_detail'),
    path('products/<int:pk>/reviews/',
         views.ReviewList.as_view(),
         name='review_list'),
    path('products/<int:pk>',
         views.ProductDetail.as_view(),
         name='product_detail'),
    path('products/',
         views.ProductList.as_view(),
         name='product_list'),
]
