
from django.http import HttpResponse
from directory.resources import OrganizationResource

def export_organization(request):
    organization_resource = OrganizationResource()
    data = organization_resource.export()
    response = HttpResponse(data.xlsx, content_type='content/xlsx')
    response['Content-Disposition'] = 'attachment; filename="organizations.xlsx"'
    return response