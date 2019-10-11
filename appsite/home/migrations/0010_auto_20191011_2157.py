# Generated by Django 2.2.4 on 2019-10-11 21:57

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191008_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='home/blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='home/blocks/embed_block.html')), ('table_block', wagtail.contrib.table_block.blocks.TableBlock(default_table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'})), ('code_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_line_numbers', wagtail.core.blocks.BooleanBlock(label='Show line numbers', required=False)), ('highlight_lines', wagtail.core.blocks.CharBlock(blank=True, help_text='1-2, 5, 9-20', label='Highlight Lines', required=False)), ('line_offset', wagtail.core.blocks.CharBlock(blank=True, help_text='40', label='Line Offset', required=False)), ('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML'), ('django', 'Django/Jinja2'), ('docker', 'Docker')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('bash_block', wagtail.core.blocks.StructBlock([('separator', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('command_line', wagtail.core.blocks.BooleanBlock(label='Show shell commands/output', required=False)), ('command_line_user', wagtail.core.blocks.CharBlock(blank=True, label='Command line user', required=False)), ('command_line_host', wagtail.core.blocks.CharBlock(blank=True, label='Command line host', required=False)), ('output_line_numbers', wagtail.core.blocks.CharBlock(blank=True, help_text='1-2, 5, 9-20', label='Output Lines', required=False)), ('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Bash'))], blank=True, verbose_name='Page Content'),
        ),
        migrations.AlterField(
            model_name='streampage',
            name='content',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.BannerPage'])), ('section_index', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.SectionIndexPage'])), ('gallery', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.GalleryPage'])), ('item_index', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.ItemIndexPage'])), ('spotlight_index', wagtail.core.blocks.PageChooserBlock(blank=True, null=True, page_type=['home.SpotlightIndexPage']))], blank=True, null=True),
        ),
    ]
