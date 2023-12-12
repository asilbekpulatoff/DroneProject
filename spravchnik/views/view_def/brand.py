
from django.http import HttpResponse
from spravchnik.resources import BrandResource

def export_brand(request):
    brand_resource = BrandResource()
    data = brand_resource.export()
    response = HttpResponse(data.xlsx, content_type='content/xlsx')
    response['Content-Disposition'] = 'attachment; filename="brands.xlsx"'
    return response