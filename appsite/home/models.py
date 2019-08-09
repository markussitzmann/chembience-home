from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import StreamField, RichTextField

from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from base.blocks import BaseStreamBlock

from home.sitedefaults import *


@register_snippet
class Button(models.Model):
    """
        Button
    """
    SIZE_CHOICES = (
        ('', 'Default'),
        ('small', 'Small'),
        ('large', 'Large'),
    )

    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, default='')
    size = models.CharField(max_length=25, choices=SIZE_CHOICES, blank=True, default='')
    icon = models.CharField(max_length=25, blank=True, default='')
    primary = models.BooleanField(default=False)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        MultiFieldPanel([
            FieldPanel('size'),
            FieldPanel('primary'),
            FieldPanel('icon'),
        ], heading="Attributes"),
    ]

    class Meta:
        verbose_name = "Button"

    def __str__(self):
        button_string = self.name + " (" + self.url + ")"
        if self.size:
            button_string = button_string + ", " + self.size
        return button_string


@register_snippet
class ActionButtons(ClusterableModel, models.Model):
    """
        Action Buttons
    """
    name = models.CharField(max_length=255)
    small = models.BooleanField(verbose_name="Small Buttons", default=False)
    fit = models.BooleanField(verbose_name="Fit Buttons", default=False)
    stacked = models.BooleanField(verbose_name="Stacked Buttons", default=False)

    panels = [
        FieldPanel('name'),
        MultiFieldPanel([
            FieldPanel('small'),
            FieldPanel('fit'),
            FieldPanel('stacked'),
        ]),
        InlinePanel('buttons', label="Action Buttons"),
    ]

    class Meta:
        verbose_name = "Action Button"
        verbose_name_plural = "Action Buttons"

    def __str__(self):
        return self.name


class ActionButton(Orderable, models.Model):
    """
        ActionButtons
    """
    action = ParentalKey('home.ActionButtons', on_delete=models.CASCADE, related_name='buttons')
    button = models.ForeignKey('home.Button', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Action Button"

    panels = [
        SnippetChooserPanel('button'),
    ]

    def __str__(self):
        return self.action.name + "->" + self.button.name


class StylingBase(models.Model):
    """

    """
    name = models.CharField(
        max_length=30,
        primary_key=True,
    )

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name


class StyleOptions(models.Model):
    """

    """
    style_id = models.AutoField(primary_key=True)
    style = models.CharField(
        max_length=30,
        choices=style_choices,
        default="style0"
    )

    panels = [
        FieldPanel('style'),
    ]

    def __str__(self):
        return self.style


class ColorOptions(models.Model):
    """

    """
    color_id = models.AutoField(primary_key=True)
    color = models.CharField(
        max_length=30,
        choices=color_choices,
        default="color0",
        null=True, blank=True
    )
    invert = models.BooleanField(
        default=False
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('color'),
            FieldPanel('invert'),
        ], heading='Basic Styling'),
    ]

    def __str__(self):
        return self.color


class OnloadFadeOptions(models.Model):
    """

    """
    onload_fade_id = models.AutoField(primary_key=True)
    onload_content_fade = models.CharField(
        max_length=30,
        choices=onload_content_fade_choices,
        default=None,
        verbose_name="Content Fade"
    )
    onload_image_fade = models.CharField(
        max_length=30,
        choices=onload_image_fade_choices,
        default=None,
        verbose_name="Image Fade"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('onload_content_fade'),
            FieldPanel('onload_image_fade'),
        ], heading='Onload fade events'),
    ]

    def __str__(self):
        return self.onload_content_fade


class OnscrollFadeOptions(models.Model):
    """

    """
    onscroll_content_fade_id = models.AutoField(primary_key=True)
    onscroll_content_fade = models.CharField(
        max_length=30,
        choices=onscroll_content_fade_choices,
        default=None,
        verbose_name="Content Fade"
    )
    onscroll_image_fade = models.CharField(
        max_length=30,
        choices=onscroll_image_fade_choices,
        default=None,
        verbose_name="Image Fade"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('onscroll_content_fade'),
            FieldPanel('onscroll_image_fade'),
        ], heading='Onscroll fade events'),
    ]

    def __str__(self):
        return self.onscroll_content_fade


class SizeOptions(models.Model):
    """
        Size Style Options
    """
    size_id = models.AutoField(primary_key=True)
    size = models.CharField(
        max_length=10,
        choices=(
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('big', 'Big'),
        ),
        default="medium"
    )

    panels = [
        FieldPanel('size'),
    ]

    def __str__(self):
        return self.size


class ContentOrientationAndAlignmentOptions(models.Model):
    """

    """
    oa_id = models.AutoField(primary_key=True)
    orientation = models.CharField(
        max_length=30,
        choices=orientation_choices,
        default="orient-left",
        verbose_name="Content to image orientation"
    )

    alignment = models.CharField(
        max_length=30,
        choices=content_align_choices,
        default="content-align-left",
        null=True,
        blank=True,
        verbose_name = "Content alignment"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('orientation'),
            FieldPanel('alignment'),
        ], heading='Content Orientation & Alignment'),
    ]


class ImagePositionOptions(models.Model):
    """

    """
    ip_id = models.AutoField(primary_key=True)
    image_position = models.CharField(
        max_length=30,
        choices=image_position_choices,
        null=True,
        blank=True,
        verbose_name="Image Position"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('image_position'),
        ], heading='Image'),
    ]


@register_snippet
class BannerStyling(StylingBase, StyleOptions, ColorOptions, ContentOrientationAndAlignmentOptions,
                    ImagePositionOptions, OnloadFadeOptions, OnscrollFadeOptions):
    """
        Banner Style Options
    """
    panels = StylingBase.panels \
             + StyleOptions.panels \
             + ColorOptions.panels \
             + ContentOrientationAndAlignmentOptions.panels \
             + ImagePositionOptions.panels \
             + OnloadFadeOptions.panels \
             + OnscrollFadeOptions.panels


@register_snippet
class GalleryStyling(StylingBase, SizeOptions):
    """
        Gallery Style Options
    """
    style = models.CharField(
        max_length=30,
        choices=style_choices[0:2],
        default="style1"
    )
    lightbox_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=32,
    )
    onload_fade_in = models.BooleanField(verbose_name="Fade in on load", default=False)
    onscroll_fade_in = models.BooleanField(verbose_name="Fade in on load", default=False)

    panels = StylingBase.panels + SizeOptions.panels + [
        FieldPanel('style'),
        FieldPanel('lightbox_button_text'),
        FieldPanel('onload_fade_in'),
        FieldPanel('onscroll_fade_in')
    ]

    class Meta:
        verbose_name = "Gallery Styling"


@register_snippet
class StylingOptions(StylingBase):
    """
        Style Options
    """
    # style = models.CharField(
    #     max_length=30,
    #     choices=style_choices,
    #     default="style1"
    # )
    orientation = models.CharField(
        max_length=30,
        choices=orientation_choices,
        default="orient-right"
    )
    content_align = models.CharField(
        max_length=30,
        choices=content_align_choices,
        default="content-align-left",
        null=True,
        blank=True
    )
    image_position = models.CharField(
        max_length=30,
        choices=image_position_choices,
        null=True,
        blank=True
    )
    onload_fade = models.CharField(
        max_length=30,
        choices=onload_fade_choices,
        null=True,
        blank=True
    )
    onscroll_fade = models.CharField(
        max_length=30,
        choices=onscroll_fade_choices,
        null=True,
        blank=True
    )
    color_choices = models.CharField(
        max_length=30,
        choices=color_choices,
        null=True,
        blank=True
    )

    panels = StylingBase.panels + [
        FieldPanel('orientation'),
        FieldPanel('content_align'),
        FieldPanel('image_position'),
        FieldPanel('onload_fade'),
        FieldPanel('onscroll_fade'),
    ]

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name_plural = "Styling Options"


class BannerPage(Page):
    """
        Banner Page
    """
    headline = models.CharField(max_length=127)
    major = RichTextField(verbose_name="Major Text", blank=True)
    minor = RichTextField(verbose_name="Minor Text", blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    styling_options = models.ForeignKey(
        'home.BannerStyling',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    actions = models.ForeignKey(
        'home.ActionButtons',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    fullscreen = models.BooleanField(verbose_name="Full Screen", default=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('major'),
        FieldPanel('minor'),
        ImageChooserPanel('image'),
        FieldPanel('styling_options'),
        FieldPanel('actions'),
        FieldPanel('fullscreen'),
    ]

    subpage_types = []

    def get_context(self, request):
        context = super(BannerPage, self).get_context(request)
        context['banner'] = self
        return context


class SectionPage(Page):
    """
        Section Page
    """
    header = models.CharField(max_length=255)
    content = StreamField(
        BaseStreamBlock(), verbose_name="Page Content", blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['SectionIndexPage']

    def get_context(self, request):
        context = super(SectionPage, self).get_context(request)
        context['section'] = self
        return context


class SectionIndexPage(Page):
    """
        Section Index Page
    """
    headline = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline', classname="full"),
        FieldPanel('introduction', classname="full"),
    ]

    subpage_types = ['SectionPage']

    def get_sections(self):
        return SectionPage.objects.live().descendant_of(self)

    def children(self):
        return self.get_children().specific().live()

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_sections(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super(SectionIndexPage, self).get_context(request)
        sections = self.paginate(request, self.get_sections())
        context['sections'] = sections
        context['section_index'] = self
        return context


class SpotlightPage(Page):
    """
        Spotlight Page
    """
    content = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    styling_options = models.ForeignKey(
        'home.StylingOptions',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    actions = models.ForeignKey(
        'home.ActionButtons',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('content'),
        FieldPanel('styling_options'),
        FieldPanel('actions'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['SpotlightIndexPage']
    subpage_types = []

    def get_context(self, request):
        context = super(SpotlightPage, self).get_context(request)
        context['spotlight'] = self
        return context


class SpotlightIndexPage(Page):
    """
        Spotlight Index Page
    """
    subpage_types = ['SpotlightPage']

    def get_spotlights(self):
        return SpotlightPage.objects.live().descendant_of(self)

    def children(self):
        return self.get_children().specific().live()

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_spotlights(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super(SpotlightIndexPage, self).get_context(request)
        spotlights = self.paginate(request, self.get_spotlights())
        context['spotlights'] = spotlights
        context['spotlight_index'] = self
        return context


class GalleryArticlePage(Page):
    """
        Gallery Article Page
    """
    headline = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    text = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    actions = models.ForeignKey(
        'home.ActionButtons',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('text'),
        ImageChooserPanel('image'),
        FieldPanel('actions'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('text'),
    ]

    parent_page_types = ['GalleryPage']
    subpage_types = []

    def get_context(self, request):
        context = super(GalleryArticlePage, self).get_context(request)
        context['gallery_article'] = self
        return context


class GalleryPage(Page):
    """
        Gallery Index Page
    """
    headline = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    styling_options = models.ForeignKey(
        'home.GalleryStyling',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('headline', classname="full"),
        FieldPanel('introduction', classname="full"),
        FieldPanel('styling_options'),
    ]

    subpage_types = ['GalleryArticlePage']

    def get_articles(self):
        return GalleryArticlePage.objects.live().descendant_of(self)

    def children(self):
        return self.get_children().specific().live()

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_articles(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super(GalleryPage, self).get_context(request)
        articles = self.paginate(request, self.get_articles())
        context['articles'] = articles
        context['gallery_index'] = self
        return context


class ItemPage(Page):
    """
        Item Page
    """
    icon = models.CharField(max_length=25, blank=True, default='')
    headline = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    text = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    actions = models.ForeignKey(
        'home.ActionButtons',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('icon'),
        FieldPanel('headline'),
        FieldPanel('text'),
        FieldPanel('actions'),

    ]

    search_fields = Page.search_fields + [
        index.SearchField('text'),
    ]

    parent_page_types = ['ItemIndexPage']
    subpage_types = []

    def get_context(self, request):
        context = super(ItemPage, self).get_context(request)
        context['item'] = self
        return context


class ItemIndexPage(Page):
    """
        Item Index Page
    """
    headline = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline', classname="full"),
        FieldPanel('introduction', classname="full"),

    ]

    subpage_types = ['ItemPage']

    def get_items(self):
        return ItemPage.objects.live().descendant_of(self)

    def children(self):
        return self.get_children().specific().live()

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_items(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super(ItemIndexPage, self).get_context(request)
        items = self.paginate(request, self.get_items())
        context['items'] = items
        context['item_index'] = self
        return context


class StreamPage(Page):
    """
        Home Stream Page
    """
    content = StreamField([
        ('banner', PageChooserBlock(target_model='home.BannerPage', null=True, blank=True)),
        ('section_index', PageChooserBlock(target_model='home.SectionIndexPage', null=True, blank=True)),
        ('gallery', PageChooserBlock(target_model='home.GalleryPage', null=True, blank=True)),
        ('item_index', PageChooserBlock(target_model='home.ItemIndexPage', null=True, blank=True)),
        ('spotlight_index', PageChooserBlock(target_model='home.SpotlightIndexPage', null=True, blank=True)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]
