from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from directory.forms import OrganizationModelForm
from directory.models import Organization


class ListOrganization(ListView):
    model = Organization
    template_name = 'directory/organization/list.html'
    context_object_name = 'organizations'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Organization.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Organization.objects.all(), key=lambda x: x.name, reverse=True)
        return Organization.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListOrganization, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            organization_filter = Organization.objects.filter(name__startswith=search)
            context['organization_filter'] = organization_filter

        return context


class DetailOrganization(DetailView):
    model = Organization
    template_name = 'directory/organization/detail.html'
    context_object_name = 'organization'


class CreateOrganization(CreateView):
    model = Organization
    # fields = ('name', )
    template_name = 'directory/organization/create_update.html'
    success_url = reverse_lazy('organization')
    form_class = OrganizationModelForm


class UpdateOrganization(UpdateView):
    model = Organization
    template_name = 'directory/organization/create_update.html'
    success_url = reverse_lazy('organization')
    context_object_name = 'organization'
    form_class = OrganizationModelForm


class DeleteOrganization(DeleteView):
    model = Organization
    success_url = reverse_lazy('organization')
    context_object_name = 'organization'
    template_name = 'directory/organization/delete.html'



