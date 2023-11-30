from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from directory.forms import EmployeeModelForm
from directory.models import Employee


class ListEmployee(ListView):
    model = Employee
    template_name = 'directory/employee/list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Employee.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Employee.objects.all(), key=lambda x: x.name, reverse=True)
        return Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListEmployee, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            employee_filter = Employee.objects.filter(name__startswith=search)
            context['employee_filter'] = employee_filter

        return context


class DetailEmployee(DetailView):
    model = Employee
    template_name = 'directory/employee/detail.html'
    context_object_name = 'employee'


class CreateEmployee(CreateView):
    model = Employee
    # fields = ('name', )
    template_name = 'directory/employee/create_update.html'
    success_url = reverse_lazy('employee')
    form_class = EmployeeModelForm


class UpdateEmployee(UpdateView):
    model = Employee
    template_name = 'directory/employee/create_update.html'
    success_url = reverse_lazy('employee')
    context_object_name = 'employee'
    form_class = EmployeeModelForm


class DeleteEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee')
    context_object_name = 'employee'
    template_name = 'directory/employee/delete.html'



