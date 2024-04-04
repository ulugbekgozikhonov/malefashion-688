from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.utils import timezone
from products.models import ProductModel, WishlistModel, ColorModel


# Create your views here.
@login_required
def add_to_wishlist(request, product_pk):
	product = ProductModel.objects.get(pk=product_pk)
	current_path_url = request.META['HTTP_REFERER']

	try:
		WishlistModel.objects.create(user=request.user, product=product)
	except Exception as exc:
		print(exc)
		WishlistModel.objects.get(user=request.user, product=product).delete()
	return redirect(current_path_url)


class ProductDetailView(DetailView):
	template_name = 'shop-details.html'
	model = ProductModel
	context_object_name = 'product'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		product = ProductModel.objects.get(pk=self.object.id)
		context['product_colors'] = product.color.all()
		context['product_sizes'] = product.size.all()
		context['related_products'] = ProductModel.objects.filter(
			category__title=self.object.category.title).exclude(pk=self.object.pk)[:4]
		return context
