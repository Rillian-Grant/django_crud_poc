from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_permission_codename
from django.core.paginator import Paginator
from django.views.generic import ListView, FormView
from .models import Item
from .forms import ItemForm


# Mixins are like decorators but for classes
class ItemListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'list.view_item'
    paginate_by = 50
    model = Item


class ItemNewView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = "list.add_item"
    form_class = ItemForm
    template_name = "list/item_form.html"  # Why needed here? Why does ListView use a default template name
    # Need to use lazy here as class based view's options are evaluated before urls are loaded
    success_url = reverse_lazy("item_list")
