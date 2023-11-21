from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import DistrictModelForm
from spravchnik.models import District


class ListDistrict(ListView):
    model = District
    template_name = 'spravchnik/district/list.html'
    context_object_name = 'districts'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(District.objects.all(), key=lambda x: x.name)
            else:
                return sorted(District.objects.all(), key=lambda x: x.name, reverse=True)
        return District.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListDistrict, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            district_filter = District.objects.filter(name__startswith=search)
            context['district_filter'] = district_filter

        return context


class DetailDistrict(DetailView):
    model = District
    template_name = 'spravchnik/district/detail.html'
    context_object_name = 'district'


class CreateDistrict(CreateView):
    model = District
    # fields = ('name', )
    template_name = 'spravchnik/district/create_update.html'
    success_url = reverse_lazy('district')
    form_class = DistrictModelForm


class UpdateDistrict(UpdateView):
    model = District
    template_name = 'spravchnik/district/create_update.html'
    success_url = reverse_lazy('district')
    context_object_name = 'district'
    form_class = DistrictModelForm


class DeleteDistrict(DeleteView):
    model = District
    success_url = reverse_lazy('district')
    context_object_name = 'district'
    template_name = 'spravchnik/district/delete.html'


