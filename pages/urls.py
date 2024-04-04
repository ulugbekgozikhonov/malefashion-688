from django.urls import path
from pages.views import HomePageView, ShopPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', ShopPageView.as_view(), name='shop'),
]
