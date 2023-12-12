from django.urls import path

from directory.views.view_class.organization import ListOrganization, DetailOrganization, DeleteOrganization, CreateOrganization, UpdateOrganization
from directory.views.view_class.employee import ListEmployee, DetailEmployee, DeleteEmployee, CreateEmployee, UpdateEmployee
from directory.views.view_class.drone import ListDrone, DetailDrone, DeleteDrone, CreateDrone, UpdateDrone
from directory.views.view_class.sensor import ListSensor, DetailSensor, DeleteSensor, CreateSensor, UpdateSensor
from directory.views.view_class.object import ListObject, DetailObject, DeleteObject, UpdateObject, CreateObject

from directory.views.view_def.organization import export_organization
urlpatterns = [
    path('organization/', ListOrganization.as_view(), name='organization'),
    path('organization/create/', CreateOrganization.as_view(), name='create_organization'),
    path('organization/<int:pk>/update/', UpdateOrganization.as_view(), name='update_organization'),
    path('organization/<int:pk>/delete/', DeleteOrganization.as_view(), name='delete_organization'),
    path('organization/<int:pk>/', DetailOrganization.as_view(), name='detail_organization'),

    path('employee/', ListEmployee.as_view(), name='employee'),
    path('employee/create/', CreateEmployee.as_view(), name='create_employee'),
    path('employee/<int:pk>/update/', UpdateEmployee.as_view(), name='update_employee'),
    path('employee/<int:pk>/delete/', DeleteEmployee.as_view(), name='delete_employee'),
    path('employee/<int:pk>/', DetailEmployee.as_view(), name='detail_employee'),

    path('drone/', ListDrone.as_view(), name='drone'),
    path('drone/create/', CreateDrone.as_view(), name='create_drone'),
    path('drone/<int:pk>/update/', UpdateDrone.as_view(), name='update_drone'),
    path('drone/<int:pk>/delete/', DeleteDrone.as_view(), name='delete_drone'),
    path('drone/<int:pk>/', DetailDrone.as_view(), name='detail_drone'),

    path('sensor/', ListSensor.as_view(), name='sensor'),
    path('sensor/create/', CreateSensor.as_view(), name='create_sensor'),
    path('sensor/<int:pk>/update/', UpdateSensor.as_view(), name='update_sensor'),
    path('sensor/<int:pk>/delete/', DeleteSensor.as_view(), name='delete_sensor'),
    path('sensor/<int:pk>/', DetailSensor.as_view(), name='detail_sensor'),

    path('object/', ListObject.as_view(), name='object'),
    path('object/create/', CreateObject.as_view(), name='create_object'),
    path('object/<int:pk>/update/', UpdateObject.as_view(), name='update_object'),
    path('object/<int:pk>/delete/', DeleteObject.as_view(), name='delete_object'),
    path('object/<int:pk>/', DetailObject.as_view(), name='detail_object'),
    
    path('export_organization/', export_organization, name='export_organization'),
]

