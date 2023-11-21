from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import PositionModelForm
from spravchnik.models import Position


class ListPosition(ListView):
    model = Position
    template_name = 'spravchnik/position/list.html'
    context_object_name = 'positions'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Position.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Position.objects.all(), key=lambda x: x.name, reverse=True)
        return Position.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListPosition, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            position_filter = Position.objects.filter(name__startswith=search)
            context['position_filter'] = position_filter

        return context


class DetailPosition(DetailView):
    model = Position
    template_name = 'spravchnik/position/detail.html'
    context_object_name = 'position'


class CreatePosition(CreateView):
    model = Position
    # fields = ('name', )
    template_name = 'spravchnik/position/create_update.html'
    success_url = reverse_lazy('position')
    form_class = PositionModelForm


class UpdatePosition(UpdateView):
    model = Position
    template_name = 'spravchnik/position/create_update.html'
    success_url = reverse_lazy('position')
    context_object_name = 'position'
    form_class = PositionModelForm


class DeletePosition(DeleteView):
    model = Position
    success_url = reverse_lazy('position')
    context_object_name = 'position'
    template_name = 'spravchnik/position/delete.html'


