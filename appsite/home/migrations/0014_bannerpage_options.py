# Generated by Django 2.1.7 on 2019-04-17 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190417_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerpage',
            name='options',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.VisualStyleOptions'),
        ),
    ]
