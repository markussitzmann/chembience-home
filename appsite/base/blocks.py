from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
    BooleanBlock)
from base.CodeBlocks import CodeBlock

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


class ExtendedCodeBlock(CodeBlock, StructBlockWithSeparator):
    """

    """
    show_line_numbers = BooleanBlock(required=False, label='Show line numbers')
    highlight_lines = CharBlock(blank=True, required=False, label='Highlight Lines', help_text='1-2, 5, 9-20')
    line_offset = CharBlock(blank=True, required=False, label='Line Offset', help_text='40')


class ExtendedBashBlock(CodeBlock, StructBlockWithSeparator):
    """

    """
    command_line = BooleanBlock(required=False, label='Show shell commands/output')
    command_line_user = CharBlock(blank=True, required=False, label='Command line user')
    command_line_host = CharBlock(blank=True, required=False, label='Command line host')
    output_line_numbers = CharBlock(blank=True, required=False, label='Output Lines', help_text='1-2, 5, 9-20')

    def __init__(self, **kwargs):

        self.INCLUDED_LANGUAGES = (
            ('bash', 'Bash'),
        )

        language_choices, language_default = self.get_language_choice_list(language='bash')

        local_blocks = [
            ('language', ChoiceBlock(
                choices=language_choices,
                help_text='Coding language',
                label='Language',
                default=language_default,
                identifier='language',
            )),
            ('code', TextBlock(label='Code', identifier='code')),
        ]
        super().__init__(local_blocks, extend=False, **kwargs)


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
    table_block = TableBlock(
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
    code_block = ExtendedCodeBlock(label='Code')
    bash_block = ExtendedBashBlock(label='Bash')




