from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
    BooleanBlock)
from wagtailcodeblock.blocks import CodeBlock

from home.sitedefaults import headline_size_choices


class StrucBlockWithSeparator(StructBlock):
    """
    """
    separator = BooleanBlock(default=False, required=False)


class ImageBlock(StrucBlockWithSeparator):
    """
    """
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"


class HeadingBlock(StrucBlockWithSeparator):
    """
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=headline_size_choices, blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StrucBlockWithSeparator):
    """
    """
    text = TextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/blockquote.html"


class BaseStreamBlock(StreamBlock):
    """
    """
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon="fa-s15",
        template="blocks/embed_block.html")
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