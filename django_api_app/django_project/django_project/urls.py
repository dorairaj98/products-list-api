from django.contrib import admin
from django.urls import path
from data_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/<shop_id>/',views.data.as_view())
]
