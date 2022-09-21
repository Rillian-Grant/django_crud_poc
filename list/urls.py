from django.urls import path

from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('new', views.ItemCreateView.as_view(), name='item_new'),
    path('<slug:pk>/edit', views.ItemUpdateView.as_view(), name='item_edit'),
    path('<slug:pk>/delete', views.ItemDeleteView.as_view(), name='item_delete'),
    path('export_csv', views.download_csv, name="download_csv")
]