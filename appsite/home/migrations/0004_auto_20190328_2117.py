# Generated by Django 2.1 on 2019-03-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190328_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotlightoptions',
            name='color',
            field=models.CharField(blank=True, choices=[('invert', 'invert'), ('color1', 'color1'), ('color2', 'color2'), ('color3', 'color3'), ('color4', 'color4'), ('color5', 'color5'), ('color6', 'color6'), ('color7', 'color7')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='spotlightoptions',
            name='color_choices',
            field=models.CharField(blank=True, choices=[('invert', 'invert'), ('color1', 'color1'), ('color2', 'color2'), ('color3', 'color3'), ('color4', 'color4'), ('color5', 'color5'), ('color6', 'color6'), ('color7', 'color7')], max_length=25, null=True),
        ),
    ]
