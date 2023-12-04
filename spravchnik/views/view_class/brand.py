from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import BrandModelForm
from spravchnik.models import Brand
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ListBrand(ListView):
    model = Brand
    template_name = 'spravchnik/brand/list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Brand.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Brand.objects.all(), key=lambda x: x.name, reverse=True)
        return Brand.objects.all()

    def get_context_data(self, **kwargs):
        brand_list = Brand.objects.all()
        context = super(ListBrand, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        page = self.request.GET.get('page', 1)

        if search is not None:
            brand_filter = Brand.objects.filter(name__startswith=search)
            context['brand_filter'] = brand_filter


        paginator = Paginator(brand_list, 2)
        try:
            brands = paginator.page(page)
            context['brands'] = brands

        except PageNotAnInteger:
            brands = paginator.page(1)
            context['brands'] = brands
        except EmptyPage:
            brands = paginator.page(paginator.num_pages)
            context['brands'] = brands

        return context


class DetailBrand(DetailView):
    model = Brand
    template_name = 'spravchnik/brand/detail.html'
    context_object_name = 'brand'


class CreateBrand(CreateView):
    model = Brand
    # fields = ('name', )
    template_name = 'spravchnik/brand/create_update.html'
    success_url = reverse_lazy('brand')
    form_class = BrandModelForm


class UpdateBrand(UpdateView):
    model = Brand
    template_name = 'spravchnik/brand/create_update.html'
    success_url = reverse_lazy('brand')
    context_object_name = 'brand'
    form_class = BrandModelForm


class DeleteBrand(DeleteView):
    model = Brand
    success_url = reverse_lazy('brand')
    context_object_name = 'brand'
    template_name = 'spravchnik/brand/delete.html'


