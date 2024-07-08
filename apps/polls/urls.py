from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get-new-purchases', views.get_new_purchases, name='get-new-purchases'),
]