from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import CountryModelForm
from spravchnik.models import Country_origin

class ListCountry(ListView):
    model = Country_origin
    template_name = 'spravchnik/country/list.html'
    context_object_name = 'countries'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted (Country_origin.objects.all(), key=lambda x: x.name)
            else:
                return sorted (Country_origin.objects.all(), key=lambda x: x.name, reverse=True)
        return Country_origin.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListCountry, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            country_filter = Country_origin.objects.filter(name__startswith=search)
            context['country_filter'] = country_filter

        return context


class DetailCountry(DetailView):
    model = Country_origin
    template_name = 'spravchnik/country/detail.html'
    context_object_name = 'country'


class CreateCountry(CreateView):
    model = Country_origin
    # fields = ('name', )
    template_name = 'spravchnik/country/create_update.html'
    success_url = reverse_lazy('country')
    form_class = CountryModelForm


class UpdateCountry(UpdateView):
    model = Country_origin
    template_name = 'spravchnik/country/create_update.html'
    success_url = reverse_lazy('country')
    context_object_name = 'country'
    form_class = CountryModelForm


class DeleteCountry(DeleteView):
    model = Country_origin
    success_url = reverse_lazy('country')
    context_object_name = 'country'
    template_name = 'spravchnik/country/delete.html'


