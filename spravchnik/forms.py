from django import forms
from django.forms import ModelForm

from spravchnik.models import Brand, Region, Category, Country_origin, Manufacturer, Position, Sensortype, District


class BrandModelForm(ModelForm):
    class Meta:
        model = Brand
        fields = ('name',)
        labels = {
            'name': 'Brand name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter brand name...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True


class RegionModelForm(ModelForm):
    class Meta:
        model = Region
        fields = ('name', 'region_code')
        labels = {
            'name': 'Region name',
            'region_code': 'Region code',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter region name...'
                }),
            'region_code': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter region code...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True
            self.fields['region_code'].required = True


class CategoryModelForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Category name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Category name...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True


class ManufacturerModelForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name',)
        labels = {
            'name': 'Manufacturer name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter manufacturer name...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True


class CountryModelForm(ModelForm):
    class Meta:
        model = Country_origin
        fields = ('name',)
        labels = {
            'name': 'Country name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Country name...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True



class PositionModelForm(ModelForm):
    class Meta:
        model = Position
        fields = ('name',)
        labels = {
            'name': 'Position name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Position name...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True


class SensortypeModelForm(ModelForm):
    class Meta:
        model = Sensortype
        fields = ('name',)
        labels = {
            'name': 'sensortype name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter sensortype name...'
                }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True



class DistrictModelForm(ModelForm):
    class Meta:
        model = District
        fields = ('name', 'district_code', 'region')
        labels = {
            'name': 'District name',
            'district_code': 'District code',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter district name...'
                })
            # 'district_code': forms.NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Enter district code...'
            #     }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = True
            self.fields['district_code'].required = True

