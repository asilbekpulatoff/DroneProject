from import_export import resources
from directory.models import Organization
from import_export.widgets import ManyToManyWidget
from import_export.fields import Field


class OrganizationResource(resources.ModelResource):

    class Meta:
        model = Organization
        fields = ('name', 'category__name', 'level', 'region__name', 'district__name','address','latitude','longitude')
        export_order = (
            'name', 'category__name', 'level', 'region__name', 'district__name', 'address', 'latitude','longitude',
        )


