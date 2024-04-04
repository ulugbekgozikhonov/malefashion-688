from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from pages.models import Banner
from products.models import *


# Create your views here.

# def home(request):
#     return render(request, 'index.html',context)

class HomePageView(ListView):
	template_name = 'index.html'
	model = Banner
	context_object_name = 'banners'

	def get_queryset(self):
		return Banner.objects.filter(status=True)


class ShopPageView(ListView):
	template_name = 'shop.html'
	model = ProductModel
	context_object_name = 'products'
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = CategoryModel.objects.all()
		context['brands'] = BrandModel.objects.all()
		context['sizes'] = SizeModel.objects.all()
		context['colors'] = ColorModel.objects.all()
		context['tags'] = TagModel.objects.all()

		return context

	def get_queryset(self):
		products = ProductModel.objects.all().order_by('price')
		category = self.request.GET.get('category')
		brand = self.request.GET.get('brand')
		size = self.request.GET.get('size')
		color = self.request.GET.get('color')
		tag = self.request.GET.get('tag')
		if category:
			products = products.filter(category__title=category)
		elif brand:
			products = products.filter(brand__title=brand)
		elif size:
			products = products.filter(size__title=brand)
		elif color:
			products = products.filter(color__name=color)
		elif tag:
			products = products.filter(tag__title=tag)

		return products

