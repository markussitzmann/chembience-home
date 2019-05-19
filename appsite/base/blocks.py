from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
    BooleanBlock)
from wagtailcodeblock.blocks import CodeBlock

from home.sitedefaults import heading_levels


class StructBlockWithSeparator(StructBlock):
    """
    """
    separator = BooleanBlock(default=False, required=False)


class ImageBlock(StructBlockWithSeparator):
    """
    """
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "home/blocks/image_block.html"


class HeadingBlock(StructBlockWithSeparator):
    """
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=heading_levels, blank=True, required=False)

    class Meta:
        icon = "title"
        template = "home/blocks/heading_block.html"


class BlockQuote(StructBlockWithSeparator):
    """
    """
    text = TextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = "fa-quote-left"
        template = "home/blocks/blockquote.html"


class BaseStreamBlock(StreamBlock):
    """
    """
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="home/blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon="fa-s15",
        template="home/blocks/embed_block.html")
    table = TableBlock(
        default_table_options={
            'minSpareRows': 0,
            'startRows': 3,
            'startCols': 3,
            'colHeaders': False,
            'rowHeaders': False,
            'contextMenu': True,
            'editor': 'text',
            'stretchH': 'all',
            'height': 108,
            'renderer': 'text',
            'autoColumnSize': False,
        }
    )
    code = CodeBlock(label='Code')



