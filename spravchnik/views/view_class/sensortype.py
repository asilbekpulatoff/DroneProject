from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import SensortypeModelForm
from spravchnik.models import Sensortype


class ListSensortype(ListView):
    model = Sensortype
    template_name = 'spravchnik/sensortype/list.html'
    context_object_name = 'sensortypes'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Sensortype.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Sensortype.objects.all(), key=lambda x: x.name, reverse=True)
        return Sensortype.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListSensortype, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            sensortype_filter = Sensortype.objects.filter(name__startswith=search)
            context['sensortype_filter'] = sensortype_filter

        return context


class DetailSensortype(DetailView):
    model = Sensortype
    template_name = 'spravchnik/sensortype/detail.html'
    context_object_name = 'sensortype'


class CreateSensortype(CreateView):
    model = Sensortype
    # fields = ('name', )
    template_name = 'spravchnik/sensortype/create_update.html'
    success_url = reverse_lazy('sensortype')
    form_class = SensortypeModelForm


class UpdateSensortype(UpdateView):
    model = Sensortype
    template_name = 'spravchnik/sensortype/create_update.html'
    success_url = reverse_lazy('sensortype')
    context_object_name = 'sensortype'
    form_class = SensortypeModelForm


class DeleteSensortype(DeleteView):
    model = Sensortype
    success_url = reverse_lazy('sensortype')
    context_object_name = 'sensortype'
    template_name = 'spravchnik/sensortype/delete.html'


