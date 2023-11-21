from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import CategoryModelForm
from spravchnik.models import Category

class ListCategory(ListView):
    model = Category
    template_name = 'spravchnik/category/list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Category.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Category.objects.all(), key=lambda x: x.name, reverse=True)
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListCategory, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            category_filter = Category.objects.filter(name__startswith=search)
            context['category_filter'] = category_filter

        return context

class DetailCategory(DetailView):
    model = Category
    template_name = 'spravchnik/category/detail.html'
    context_object_name = 'category'


class CreateCategory(CreateView):
    model = Category
    # fields = ('name', )
    template_name = 'spravchnik/category/create_update.html'
    success_url = reverse_lazy('category')
    form_class = CategoryModelForm


class UpdateCategory(UpdateView):
    model = Category
    template_name = 'spravchnik/category/create_update.html'
    success_url = reverse_lazy('category')
    context_object_name = 'category'
    form_class = CategoryModelForm


class DeleteCategory(DeleteView):
    model = Category
    success_url = reverse_lazy('category')
    context_object_name = 'category'
    template_name = 'spravchnik/category/delete.html'


