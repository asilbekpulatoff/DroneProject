from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import RegionModelForm, BrandModelForm
from spravchnik.models import Region


class ListRegion(ListView):
    model = Region
    template_name = 'spravchnik/region/list.html'
    context_object_name = 'regions'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Region.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Region.objects.all(), key=lambda x: x.name, reverse=True)
        return Region.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListRegion, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            region_filter = Region.objects.filter(name__startswith=search)
            context['region_filter'] = region_filter

        return context


class DetailRegion(DetailView):
    model = Region
    template_name = 'spravchnik/region/detail.html'
    context_object_name = 'region'


class CreateRegion(CreateView):
    model = Region
    # fields = ('name', )
    template_name = 'spravchnik/region/create_update.html'
    success_url = reverse_lazy('region')
    form_class = RegionModelForm


class UpdateRegion(UpdateView):
    model = Region
    template_name = 'spravchnik/region/create_update.html'
    success_url = reverse_lazy('region')
    context_object_name = 'region'
    form_class = RegionModelForm


class DeleteRegion(DeleteView):
    model = Region
    success_url = reverse_lazy('region')
    context_object_name = 'region'
    template_name = 'spravchnik/region/delete.html'


