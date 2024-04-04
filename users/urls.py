from django.urls import path
from users.views import SignUpView, SignInView, WishListView, sign_in, sign_up, sign_out

app_name = 'users'
urlpatterns = [
	# path('signup/', SignUpView.as_view(), name='signup'),
	# path('signin/', SignInView.as_view(), name='signin'),
	path('signup/', sign_up, name='signup'),
	path('signin/', sign_in, name='signin'),
	path('signout/', sign_out, name='signout'),
	path('wishlists/', WishListView.as_view(), name='wishlists'),
]
