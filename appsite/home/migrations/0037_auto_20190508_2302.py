# Generated by Django 2.2 on 2019-05-08 23:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20190508_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeblockpage',
            name='content',
            field=wagtail.core.fields.StreamField([('banner_block', wagtail.core.blocks.PageChooserBlock(page_type=['home.BannerPage', 'home.SectionIndexPage'], template='home/blocks/page_builder_block.html'))], blank=True, verbose_name='Page Content'),
        ),
    ]
