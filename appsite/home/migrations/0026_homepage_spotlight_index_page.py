# Generated by Django 2.2 on 2019-05-03 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0025_auto_20190429_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='spotlight_index_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Sections'),
        ),
    ]
