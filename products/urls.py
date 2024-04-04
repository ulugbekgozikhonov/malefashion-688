from django.urls import path
from products.views import add_to_wishlist, ProductDetailView

app_name = 'products'
urlpatterns = [
	path('<int:product_pk>/add-to-wishlist/', add_to_wishlist, name='add_to_wishlist'),
	path('<int:pk>/details/', ProductDetailView.as_view(), name='product_detail'),
]
