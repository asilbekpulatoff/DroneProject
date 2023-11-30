from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from directory.forms import DroneModelForm
from directory.models import Drone


class ListDrone(ListView):
    model = Drone
    template_name = 'directory/drone/list.html'
    context_object_name = 'drones'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Drone.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Drone.objects.all(), key=lambda x: x.name, reverse=True)
        return Drone.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListDrone, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            drone_filter = Drone.objects.filter(name__startswith=search)
            context['drone_filter'] = drone_filter

        return context


class DetailDrone(DetailView):
    model = Drone
    template_name = 'directory/drone/detail.html'
    context_object_name = 'drone'


class CreateDrone(CreateView):
    model = Drone
    # fields = ('name', )
    template_name = 'directory/drone/create_update.html'
    success_url = reverse_lazy('drone')
    form_class = DroneModelForm


class UpdateDrone(UpdateView):
    model = Drone
    template_name = 'directory/drone/create_update.html'
    success_url = reverse_lazy('drone')
    context_object_name = 'drone'
    form_class = DroneModelForm


class DeleteDrone(DeleteView):
    model = Drone
    success_url = reverse_lazy('drone')
    context_object_name = 'drone'
    template_name = 'directory/drone/delete.html'



