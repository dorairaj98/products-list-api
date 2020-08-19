from django.contrib import admin
from .models import shop, category, product, media

admin.site.register(shop)
admin.site.register(category)
admin.site.register(product)
admin.site.register(media)