from django.urls import path

from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('new', views.ItemNewView.as_view(), name='item_new'),
]