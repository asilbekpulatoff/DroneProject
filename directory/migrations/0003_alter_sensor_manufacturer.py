# Generated by Django 4.2.6 on 2023-11-25 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spravchnik', '0002_alter_category_options_alter_country_origin_options_and_more'),
        ('directory', '0002_alter_drone_production_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spravchnik.manufacturer'),
        ),
    ]