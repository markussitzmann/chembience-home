# Generated by Django 2.2.4 on 2019-08-12 21:04

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionButtons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('small', models.BooleanField(default=False, verbose_name='Small Buttons')),
                ('fit', models.BooleanField(default=False, verbose_name='Fit Buttons')),
                ('stacked', models.BooleanField(default=False, verbose_name='Stacked Buttons')),
            ],
            options={
                'verbose_name': 'Action Button',
                'verbose_name_plural': 'Action Buttons',
            },
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, default='', max_length=255)),
                ('size', models.CharField(blank=True, choices=[('', 'Default'), ('small', 'Small'), ('large', 'Large')], default='', max_length=25)),
                ('icon', models.CharField(blank=True, default='', max_length=25)),
                ('primary', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Button',
            },
        ),
        migrations.CreateModel(
            name='ColorOptions',
            fields=[
                ('color_id', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(blank=True, choices=[('color0', 'color 0'), ('color1', 'color 1'), ('color2', 'color 2'), ('color3', 'color 3'), ('color4', 'color 4'), ('color5', 'color 5'), ('color6', 'color 6'), ('color7', 'color 7')], default='color0', max_length=30, null=True)),
                ('invert', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContentAlignmentOptions',
            fields=[
                ('alignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('alignment', models.CharField(blank=True, choices=[('content-align-left', 'left'), ('content-align-center', 'center'), ('content-align-right', 'right')], default='content-align-left', max_length=30, null=True, verbose_name='Alignment')),
            ],
        ),
        migrations.CreateModel(
            name='ContentOrientationOptions',
            fields=[
                ('orientation_id', models.AutoField(primary_key=True, serialize=False)),
                ('orientation', models.CharField(choices=[('orient-left', 'left'), ('orient-center', 'center'), ('orient-right', 'right')], default='orient-left', max_length=30, verbose_name='Orientation')),
            ],
        ),
        migrations.CreateModel(
            name='ImagePositionOptions',
            fields=[
                ('ip_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_position', models.CharField(blank=True, choices=[('image-position-left', 'left'), ('image-position-center', 'center'), ('image-position-right', 'right')], default='image-position-left', max_length=30, null=True, verbose_name='Image Position')),
            ],
        ),
        migrations.CreateModel(
            name='OnloadContentFadeOptions',
            fields=[
                ('onload_content_fade_id', models.AutoField(primary_key=True, serialize=False)),
                ('onload_content_fade', models.CharField(blank=True, choices=[(None, 'none'), ('onload-content-fade-up', 'up'), ('onload-content-fade-down', 'down'), ('onload-content-fade-left', 'left'), ('onload-content-fade-right', 'right'), ('onload-content-fade-in', 'in')], default=None, max_length=30, null=True, verbose_name='Onload Fade')),
            ],
        ),
        migrations.CreateModel(
            name='OnloadImageFadeOptions',
            fields=[
                ('onload_image_fade_id', models.AutoField(primary_key=True, serialize=False)),
                ('onload_image_fade', models.CharField(blank=True, choices=[(None, 'none'), ('onload-image-fade-up', 'up'), ('onload-image-fade-down', 'down'), ('onload-image-fade-left', 'left'), ('onload-image-fade-right', 'right'), ('onload-image-fade-in', 'in')], default=None, max_length=30, null=True, verbose_name='Image Fade')),
            ],
        ),
        migrations.CreateModel(
            name='OnscrollContentFadeOptions',
            fields=[
                ('onscroll_content_fade_id', models.AutoField(primary_key=True, serialize=False)),
                ('onscroll_content_fade', models.CharField(blank=True, choices=[(None, 'none'), ('onscroll-content-fade-up', 'up'), ('onscroll-content-fade-down', 'down'), ('onscroll-content-fade-left', 'left'), ('onscroll-content-fade-right', 'right'), ('onscroll-content-fade-in', 'in')], default=None, max_length=30, null=True, verbose_name='Content Fade')),
            ],
        ),
        migrations.CreateModel(
            name='OnscrollImageFadeOptions',
            fields=[
                ('onscroll_image_fade_id', models.AutoField(primary_key=True, serialize=False)),
                ('onscroll_image_fade', models.CharField(blank=True, choices=[(None, 'none'), ('onscroll-image-fade-up', 'up'), ('onscroll-image-fade-down', 'down'), ('onscroll-image-fade-left', 'left'), ('onscroll-image-fade-right', 'right'), ('onscroll-image-fade-in', 'in')], default=None, max_length=30, null=True, verbose_name='Image Fade')),
            ],
        ),
        migrations.CreateModel(
            name='ScreenOptions',
            fields=[
                ('screen_id', models.AutoField(primary_key=True, serialize=False)),
                ('screen', models.CharField(blank=True, choices=[(None, 'none'), ('fullscreen', 'full screen'), ('halfscreen', 'half screen')], default='none', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SectionIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(blank=True, max_length=255, null=True)),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SectionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header', models.CharField(max_length=255)),
                ('content', wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='home/blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='home/blocks/embed_block.html')), ('table', wagtail.contrib.table_block.blocks.TableBlock(default_table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'})), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code'))], blank=True, verbose_name='Page Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SizeOptions',
            fields=[
                ('size_id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('big', 'Big')], default='medium', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SpotlightIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StreamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.BannerPage'])), ('section_index', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.SectionIndexPage'])), ('gallery', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.GalleryPage'])), ('item_index', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.ItemIndexPage'])), ('spotlight_index', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.SpotlightIndexPage']))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StyleOptions',
            fields=[
                ('style_id', models.AutoField(primary_key=True, serialize=False)),
                ('style', models.CharField(choices=[('style1', 'No. 1'), ('style2', 'No. 2'), ('style3', 'No. 3'), ('style4', 'No. 4'), ('style5', 'No. 5'), ('style6', 'No. 6'), ('style7', 'No. 7')], default='style0', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StylingBase',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='BannerStyling',
            fields=[
                ('screenoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ScreenOptions')),
                ('onscrollimagefadeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.OnscrollImageFadeOptions')),
                ('onscrollcontentfadeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.OnscrollContentFadeOptions')),
                ('onloadimagefadeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.OnloadImageFadeOptions')),
                ('onloadcontentfadeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.OnloadContentFadeOptions')),
                ('imagepositionoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ImagePositionOptions')),
                ('contentalignmentoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ContentAlignmentOptions')),
                ('contentorientationoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ContentOrientationOptions')),
                ('coloroptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ColorOptions')),
                ('styleoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.StyleOptions')),
                ('stylingbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.StylingBase')),
            ],
            options={
                'verbose_name': 'Banner Styling',
            },
            bases=('home.stylingbase', 'home.styleoptions', 'home.coloroptions', 'home.contentorientationoptions', 'home.contentalignmentoptions', 'home.imagepositionoptions', 'home.onloadcontentfadeoptions', 'home.onloadimagefadeoptions', 'home.onscrollcontentfadeoptions', 'home.onscrollimagefadeoptions', 'home.screenoptions'),
        ),
        migrations.CreateModel(
            name='GalleryStyling',
            fields=[
                ('sizeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.SizeOptions')),
                ('styleoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.StyleOptions')),
                ('stylingbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.StylingBase')),
                ('lightbox_button_text', models.CharField(blank=True, max_length=32, null=True)),
                ('onload_fade_in', models.BooleanField(default=False, verbose_name='Fade In on Load')),
                ('onscroll_fade_in', models.BooleanField(default=False, verbose_name='Fade In on Scroll')),
            ],
            options={
                'verbose_name': 'Gallery Styling',
            },
            bases=('home.stylingbase', 'home.styleoptions', 'home.sizeoptions'),
        ),
        migrations.CreateModel(
            name='ItemStyling',
            fields=[
                ('sizeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.SizeOptions')),
                ('styleoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.StyleOptions')),
                ('stylingbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.StylingBase')),
                ('onload_fade_in', models.BooleanField(default=False, verbose_name='Fade In on Load')),
                ('onscroll_fade_in', models.BooleanField(default=False, verbose_name='Fade In on Scroll')),
            ],
            options={
                'verbose_name': 'Item Styling',
            },
            bases=('home.stylingbase', 'home.styleoptions', 'home.sizeoptions'),
        ),
        migrations.CreateModel(
            name='SpotlightStyling',
            fields=[
                ('screenoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ScreenOptions')),
                ('onscrollimagefadeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.OnscrollImageFadeOptions')),
                ('onscrollcontentfadeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.OnscrollContentFadeOptions')),
                ('onloadimagefadeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.OnloadImageFadeOptions')),
                ('onloadcontentfadeoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.OnloadContentFadeOptions')),
                ('imagepositionoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ImagePositionOptions')),
                ('contentalignmentoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ContentAlignmentOptions')),
                ('contentorientationoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ContentOrientationOptions')),
                ('coloroptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.ColorOptions')),
                ('styleoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.StyleOptions')),
                ('stylingbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.StylingBase')),
            ],
            options={
                'verbose_name': 'Spotlight Styling',
            },
            bases=('home.stylingbase', 'home.styleoptions', 'home.coloroptions', 'home.contentorientationoptions', 'home.contentalignmentoptions', 'home.imagepositionoptions', 'home.onloadcontentfadeoptions', 'home.onloadimagefadeoptions', 'home.onscrollcontentfadeoptions', 'home.onscrollimagefadeoptions', 'home.screenoptions'),
        ),
        migrations.CreateModel(
            name='ItemPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('icon', models.CharField(blank=True, default='', max_length=30)),
                ('headline', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(blank=True, help_text='Text to describe the page')),
                ('actions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.ActionButtons')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GalleryArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(blank=True, help_text='Text to describe the page')),
                ('actions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.ActionButtons')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ActionButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('action', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='buttons', to='home.ActionButtons')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.Button')),
            ],
            options={
                'verbose_name': 'Action Button',
            },
        ),
        migrations.CreateModel(
            name='SpotlightPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.RichTextField(blank=True)),
                ('actions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.ActionButtons')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('styling_options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.SpotlightStyling')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ItemIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(blank=True, max_length=255, null=True)),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('styling_options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.ItemStyling')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GalleryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(blank=True, max_length=255, null=True)),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('styling_options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.GalleryStyling')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BannerPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(max_length=127)),
                ('major', wagtail.core.fields.RichTextField(blank=True, verbose_name='Major Text')),
                ('minor', wagtail.core.fields.RichTextField(blank=True, verbose_name='Minor Text')),
                ('actions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.ActionButtons')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('styling_options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.BannerStyling')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
