import csv

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_permission_codename
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm


# Mixins are like decorators but for classes
class ItemListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'list.view_item'
    paginate_by = 50
    model = Item
    #queryset = Item.objects.all().order_by("-id") # Already set as default in model's meta


class ItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "list.add_item"
    model = Item
    fields = ("name", "txt1", "num1", "num2", "num3")
    success_url = reverse_lazy("item_list")


class ItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "list.edit_item"
    model = Item
    fields = ("name", "txt1", "num1", "num2", "num3")
    success_url = reverse_lazy("item_list")


class ItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "list.delete_item"
    model = Item
    success_url = reverse_lazy("item_list")


@login_required()
@permission_required("list.download_csv")
def download_csv(request):
    queryset = Item.objects.all()
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = ["id", "name", "txt1", "num1", "num2", "num3"]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
