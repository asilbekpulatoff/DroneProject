from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import ManufacturerModelForm
from spravchnik.models import Manufacturer

class ListManufacturer(ListView):
    model = Manufacturer
    template_name = 'spravchnik/manufacturer/list.html'
    context_object_name = 'manufacturers'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted (Manufacturer.objects.all(), key=lambda x: x.name)
            else:
                return sorted (Manufacturer.objects.all(), key=lambda x: x.name, reverse=True)
        return Manufacturer.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListManufacturer, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            manufacturer_filter = Manufacturer.objects.filter(name__startswith=search)
            context['manufacturer_filter'] = manufacturer_filter

        return context


class DetailManufacturer(DetailView):
    model = Manufacturer
    template_name = 'spravchnik/manufacturer/detail.html'
    context_object_name = 'manufacturer'


class CreateManufacturer(CreateView):
    model = Manufacturer
    # fields = ('name', )
    template_name = 'spravchnik/manufacturer/create_update.html'
    success_url = reverse_lazy('manufacturer')
    form_class = ManufacturerModelForm


class UpdateManufacturer(UpdateView):
    model = Manufacturer
    template_name = 'spravchnik/manufacturer/create_update.html'
    success_url = reverse_lazy('manufacturer')
    context_object_name = 'manufacturer'
    form_class = ManufacturerModelForm


class DeleteManufacturer(DeleteView):
    model = Manufacturer
    success_url = reverse_lazy('manufacturer')
    context_object_name = 'manufacturer'
    template_name = 'spravchnik/manufacturer/delete.html'


