
from django.http import HttpResponse
from spravchnik.resources import DistrictResource

def export_district(request):
    district_resource = DistrictResource()
    data = district_resource.export()
    response = HttpResponse(data.xlsx, content_type='content/xlsx')
    response['Content-Disposition'] = 'attachment; filename="districts.xlsx"'
    return response