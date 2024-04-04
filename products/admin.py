from django.contrib import admin
from products.models import *

# Register your models here.


# @admin.register(CategoryModel)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_at']


admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(ColorModel)
admin.site.register(SizeModel)
admin.site.register(TagModel)
admin.site.register(BrandModel)
admin.site.register(ProductImagesModel)


@admin.register(WishlistModel)
class WishlistAdminModel(admin.ModelAdmin):
	list_display = ['product', 'user']
