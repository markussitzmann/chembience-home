# Generated by Django 2.2 on 2019-05-05 17:24

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20190505_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='home/blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='home/blocks/embed_block.html')), ('table', wagtail.contrib.table_block.blocks.TableBlock(default_table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'})), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code'))], blank=True, verbose_name='Page Content'),
        ),
        migrations.AlterField(
            model_name='spotlightpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='home/blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='home/blocks/embed_block.html')), ('table', wagtail.contrib.table_block.blocks.TableBlock(default_table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'})), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code'))], blank=True, verbose_name='Page Content'),
        ),
    ]
