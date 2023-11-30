from django import forms
from django.forms import ModelForm

from directory.models import Organization, Employee, Drone, Sensor, Object


class OrganizationModelForm(ModelForm):
    class Meta:
        model = Organization
        fields = ('name', 'category', 'level', 'region', 'district','address', 'latitude', 'longitude')
        labels = {
            'name': 'Organization name',
            'level': 'Level name',
            'address':'Address name',
            'latitude':'Latitude name',
            'longitude':'Logitude number'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter region name...'
                }),
            'level': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter level name...'
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter address name...'
                }),
            'latitude': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter latitude name...'
                }),
            'longitude': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter longitude number...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True
            self.fields['level'].required = True
            self.fields['latitude'].required = True
            self.fields['longitude'].required = True


class EmployeeModelForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('brand', 'first_name', 'last_name', 'surname', 'organization','position', 'birthday', 'place_of_birth', 'pasport_data')
        labels = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'surname':'surname',
            'birthday':'birthday',
            'place_of_birth':'place_of_birth',
            'pasport_data':'pasport_data'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter firstname...'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter lastname...'
                }),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter surname...'
                }),
            'birthday': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter birthday day...'
                }),
            'place_of_birth': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter place of birth...'
                }),
            'pasport_data': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter passport number...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
            self.fields['surname'].required = True
            self.fields['birthday'].required = True
            self.fields['place_of_birth'].required = True
            self.fields['pasport_data'].required = True



class DroneModelForm(ModelForm):
    class Meta:
        model = Drone
        fields = ('drone_id', 'name', 'brand', 'model', 'manufacturer','country_origin', 'production_year', 'mood', 'owner', 'operator', 'status')
        labels = {
            'drone_id': 'drone_id',
            'name': 'name',
            'model':'model',
            'production_year':'production_year',
            'mood':'mood',
            'status':'status'
        }
        widgets = {
            'drone_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter drone id...'
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter drone name...'
                }),
            'model': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter drone model...'
                }),
            'production_year': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter production year...'
                }),
            'mood': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter mood...'
                }),
            'status': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter drone status...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['drone_id'].required = True
            self.fields['name'].required = True
            self.fields['model'].required = True
            self.fields['production_year'].required = True
            self.fields['mood'].required = True
            self.fields['status'].required = True



class SensorModelForm(ModelForm):
    class Meta:
        model = Sensor
        fields = ('sensor_id', 'name', 'type', 'model', 'manufacturer','country_origin', 'production_year', 'condition', 'status', 'type_host', 'host_id')
        labels = {
            'sensor_id': 'sensor_id',
            'name': 'name',
            'type':'type',
            'model':'model',
            'production_year':'production_year',
            'condition':'condition',
            'status':'status',
            'type_host':'type_host',
            'host_id':'host_id',
        }
        widgets = {
            'sensor_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter sensor id...'
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter sensor name...'
                }),
            'model': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter sensor model...'
                }),
            'production_year': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter sensor production year...'
                }),
            'condition': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter condition...'
                }),
            'status': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter drone status...'
                }),
            'type_host': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter type host...'
                }),
            'host_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter host_id...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['sensor_id'].required = True
            self.fields['name'].required = True
            self.fields['model'].required = True
            self.fields['production_year'].required = True
            self.fields['condition'].required = True
            self.fields['status'].required = True
            self.fields['type_host'].required = True
            self.fields['host_id'].required = True


class ObjectModelForm(ModelForm):
    class Meta:
        model = Object
        fields = ('name', 'category', 'level', 'region','district', 'address', 'latitude', 'longitude')
        labels = {
            'name': 'name',
            'level':'level',
            'address':'address',
            'latitude':'Latitude name',
            'longitude':'Logitude number'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter drone name...'
                }),
            'level': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter object level...'
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter address...'
                }),
            'latitude': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter latitude...'
                }),
            'longetude': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter longetude...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True
            self.fields['level'].required = True
            self.fields['address'].required = True
            self.fields['latitude'].required = True
            self.fields['longetude'].required = True

