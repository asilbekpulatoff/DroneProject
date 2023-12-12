from import_export import resources
from spravchnik.models import District, Brand
from import_export.widgets import ManyToManyWidget
from import_export.fields import Field


class DistrictResource(resources.ModelResource):

    class Meta:
        model = District
        fields = ('name', 'district_code', 'region__name')
        export_order = (
            'name', 'district_code', 'region__name'
        )

class BrandResource(resources.ModelResource):

    class Meta:
        model = Brand
        fields = ('name', )
