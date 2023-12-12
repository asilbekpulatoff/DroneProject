from django.urls import path

from spravchnik.views.view_class.brand import DeleteBrand, ListBrand, CreateBrand, UpdateBrand, DetailBrand
from spravchnik.views.view_class.region import ListRegion, DetailRegion, CreateRegion, UpdateRegion, DeleteRegion
from spravchnik.views.view_class.category import ListCategory,DeleteCategory, UpdateCategory, DetailCategory, CreateCategory
from spravchnik.views.view_class.country import ListCountry, DeleteCountry, DetailCountry, CreateCountry, UpdateCountry
from spravchnik.views.view_class.manufacture import ListManufacturer, DeleteManufacturer, DetailManufacturer, CreateManufacturer, UpdateManufacturer
from spravchnik.views.view_class.position import ListPosition, DetailPosition, DeletePosition, UpdatePosition, CreatePosition
from spravchnik.views.view_class.sensortype import ListSensortype, DetailSensortype, DeleteSensortype, CreateSensortype, UpdateSensortype
from spravchnik.views.view_class.district import ListDistrict, DetailDistrict, DeleteDistrict, CreateDistrict, UpdateDistrict

from spravchnik.views.view_def.district import export_district
from spravchnik.views.view_def.brand import export_brand

# from spravchnik.views import index, delete_brand, create_brand, update_brand

urlpatterns = [
    path('brand/', ListBrand.as_view(), name='brand'),
    path('brand/create/', CreateBrand.as_view(), name='create_brand'),
    path('brand/<int:pk>/update/', UpdateBrand.as_view(), name='update_brand'),
    path('brand/<int:pk>/delete/', DeleteBrand.as_view(), name='delete_brand'),
    path('brand/<int:pk>/', DetailBrand.as_view(), name='detail_brand'),

    path('region/', ListRegion.as_view(), name='region'),
    path('region/create/', CreateRegion.as_view(), name='create_region'),
    path('region/<int:pk>/update/', UpdateRegion.as_view(), name='update_region'),
    path('region/<int:pk>/delete/', DeleteRegion.as_view(), name='delete_region'),
    path('region/<int:pk>/', DetailRegion.as_view(), name='detail_region'),

    path('category/', ListCategory.as_view(), name='category'),
    path('category/create/', CreateCategory.as_view(), name='create_category'),
    path('category/<int:pk>/update/', UpdateCategory.as_view(), name='update_category'),
    path('category/<int:pk>/delete/', DeleteCategory.as_view(), name='delete_category'),
    path('category/<int:pk>/', DetailCategory.as_view(), name='detail_category'),
    
    path('country/', ListCountry.as_view(), name='country'),
    path('country/create/', CreateCountry.as_view(), name='create_country'),
    path('country/<int:pk>/update/', UpdateCountry.as_view(), name='update_country'),
    path('country/<int:pk>/delete/', DeleteCountry.as_view(), name='delete_country'),
    path('country/<int:pk>/', DetailCountry.as_view(), name='detail_country'),

    path('manufacturer/', ListManufacturer.as_view(), name='manufacturer'),
    path('manufacturer/create/', CreateManufacturer.as_view(), name='create_manufacturer'),
    path('manufacturer/<int:pk>/update/', UpdateManufacturer.as_view(), name='update_manufacturer'),
    path('manufacturer/<int:pk>/delete/', DeleteManufacturer.as_view(), name='delete_manufacturer'),
    path('manufacturer/<int:pk>/', DetailManufacturer.as_view(), name='detail_manufacturer'),

    path('position/', ListPosition.as_view(), name='position'),
    path('position/create/', CreatePosition.as_view(), name='create_position'),
    path('position/<int:pk>/update/', UpdatePosition.as_view(), name='update_position'),
    path('position/<int:pk>/delete/', DeletePosition.as_view(), name='delete_position'),
    path('position/<int:pk>/', DetailPosition.as_view(), name='detail_position'),

    path('sensortype/', ListSensortype.as_view(), name='sensortype'),
    path('sensortype/create/', CreateSensortype.as_view(), name='create_sensortype'),
    path('sensortype/<int:pk>/update/', UpdateSensortype.as_view(), name='update_sensortype'),
    path('sensortype/<int:pk>/delete/', DeleteSensortype.as_view(), name='delete_sensortype'),
    path('sensortype/<int:pk>/', DetailSensortype.as_view(), name='detail_sensortype'),

    path('district/', ListDistrict.as_view(), name='district'),
    path('district/create/', CreateDistrict.as_view(), name='create_district'),
    path('district/<int:pk>/update/', UpdateDistrict.as_view(), name='update_district'),
    path('district/<int:pk>/delete/', DeleteDistrict.as_view(), name='delete_district'),
    path('district/<int:pk>/', DetailDistrict.as_view(), name='detail_district'),

    path('export_brand/', export_brand, name='export_brand'),
    path('export_district/', export_district, name='export_district')
]
