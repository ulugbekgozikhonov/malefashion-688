from django.contrib.auth.models import User
from django.db import models
from products.validators import rating_validation
from django.utils import timezone


# Create your models here.

class Base(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class CategoryModel(Base):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"


class BrandModel(Base):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Brand"
		verbose_name_plural = "Brands"


class SizeModel(models.Model):
	title = models.CharField(max_length=25)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Size"
		verbose_name_plural = "Sizes"


class ColorModel(models.Model):
	name = models.CharField(max_length=25)
	color_code = models.CharField(max_length=55)

	def __str__(self):
		return f"{self.name}|{self.color_code}"

	class Meta:
		verbose_name = "Color"
		verbose_name_plural = "Colors"


class TagModel(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tags"


class ProductModel(Base):
	name = models.CharField(max_length=55)
	price = models.FloatField()
	description = models.TextField()
	image = models.ImageField(upload_to='products/')
	rating = models.PositiveIntegerField(default=1, validators=[rating_validation])
	discount = models.PositiveIntegerField(default=0)
	category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
	brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='products')
	size = models.ManyToManyField(SizeModel)
	color = models.ManyToManyField(ColorModel)
	tag = models.ManyToManyField(TagModel)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def is_new(self):
		diff = (timezone.now() - self.created_at).days
		return diff <= 3


class ProductImagesModel(models.Model):
	image = models.ImageField(upload_to='product/images')
	product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="images")

	class Meta:
		verbose_name = "Product Image"
		verbose_name_plural = "Product Images"

	def __str__(self) -> str:
		return self.product.name


class WishlistModel(Base):
	product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Wishlist'
		verbose_name_plural = 'Wishlists'
		unique_together = ['user', 'product']

	def __str__(self):
		return f"{self.user.username} | {self.product.name}"
