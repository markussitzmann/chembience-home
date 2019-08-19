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
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, default='')
    size = models.CharField(max_length=25, choices=(
        ('', 'Default'),
        ('small', 'Small'),
        ('large', 'Large'),
    ), blank=True, default='')
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
        ], heading="Action Button Group Settings"),
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


@register_snippet
class IconButtons(ClusterableModel, models.Model):
    """
        Icon Buttons
    """
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
        InlinePanel('buttons', label="Icon Buttons"),
    ]

    class Meta:
        verbose_name = "Icon Button"
        verbose_name_plural = "Icon Buttons"

    def __str__(self):
        return self.name


class IconButton(Orderable, models.Model):
    """
        IconButtons
    """
    icon = ParentalKey('home.IconButtons', on_delete=models.CASCADE, related_name='buttons')
    button = models.ForeignKey('home.Button', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Icon Button"

    panels = [
        SnippetChooserPanel('button'),
    ]

    def __str__(self):
        return self.icon.name + "->" + self.button.name



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


class OnloadContentFadeOptions(models.Model):
    """

    """
    onload_content_fade_id = models.AutoField(primary_key=True)
    onload_content_fade = models.CharField(
        max_length=30,
        choices=onload_content_fade_choices,
        default=None,
        null=True,
        blank=True,
        verbose_name="Onload Fade"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('onload_content_fade'),
        ], heading='Onload Content Fade Events'),
    ]

    def __str__(self):
        return self.onload_content_fade


class OnloadImageFadeOptions(models.Model):
    """

    """
    onload_image_fade_id = models.AutoField(primary_key=True)
    onload_image_fade = models.CharField(
        max_length=30,
        choices=onload_content_fade_choices,
        default=None,
        null=True,
        blank=True,
        verbose_name="Onload Image Fade"
    )
    onload_image_fade = models.CharField(
        max_length=30,
        choices=onload_image_fade_choices,
        default=None,
        null=True,
        blank=True,
        verbose_name="Image Fade"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('onload_image_fade'),
        ], heading='Onload Image Fade Events'),
    ]

    def __str__(self):
        return self.onload_image_fade


class OnscrollContentFadeOptions(models.Model):
    """

    """
    onscroll_content_fade_id = models.AutoField(primary_key=True)
    onscroll_content_fade = models.CharField(
        max_length=30,
        choices=onscroll_content_fade_choices,
        default=None,
        null=True,
        blank=True,
        verbose_name="Content Fade"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('onscroll_content_fade'),
        ], heading='Onscroll Fade Events'),
    ]

    def __str__(self):
        return self.onscroll_content_fade


class OnscrollImageFadeOptions(models.Model):
    """

    """
    onscroll_image_fade_id = models.AutoField(primary_key=True)
    onscroll_image_fade = models.CharField(
        max_length=30,
        choices=onscroll_image_fade_choices,
        default=None,
        null=True,
        blank=True,
        verbose_name="Image Fade"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('onscroll_image_fade'),
        ], heading='Onscroll Image Fade Events'),
    ]

    def __str__(self):
        return self.onscroll_image_fade


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
        default='medium'
    )

    panels = [
        FieldPanel('size'),
    ]

    def __str__(self):
        return self.size


class ContentOrientationOptions(models.Model):
    """

    """
    orientation_id = models.AutoField(primary_key=True)
    orientation = models.CharField(
        max_length=30,
        choices=orientation_choices,
        default='orient-left',
        verbose_name="Orientation"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('orientation'),
        ], heading="Content to Image Orientation"),
    ]


class ContentAlignmentOptions(models.Model):
    """

    """
    alignment_id = models.AutoField(primary_key=True)
    alignment = models.CharField(
        max_length=30,
        choices=alignment_choices,
        default='content-align-left',
        null=True,
        blank=True,
        verbose_name="Alignment"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('alignment'),
        ], heading='Content Text Alignment'),
    ]


class ImagePositionOptions(models.Model):
    """

    """
    ip_id = models.AutoField(primary_key=True)
    image_position = models.CharField(
        max_length=30,
        choices=image_position_choices,
        default='image-position-left',
        null=True,
        blank=True,
        verbose_name="Image Position"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('image_position'),
        ], heading='Image'),
    ]


class ScreenOptions(models.Model):
    """

    """
    screen_id = models.AutoField(primary_key=True)
    screen = models.CharField(
        max_length=30,
        choices=(
            (None, 'none'),
            ('fullscreen', 'full screen'),
            ('halfscreen', 'half screen')
        ),
        default="none",
        null=True,
        blank=True
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('screen'),
        ], heading='Screen Size'),
    ]

    def __str__(self):
        return self.screen


@register_snippet
class BannerStyling(StylingBase, StyleOptions, ColorOptions, ContentOrientationOptions, ContentAlignmentOptions,
                ImagePositionOptions, OnloadContentFadeOptions, OnloadImageFadeOptions, OnscrollContentFadeOptions,
                OnscrollImageFadeOptions, ScreenOptions):
    """
        Banner Style Options
    """
    panels = StylingBase.panels \
             + StyleOptions.panels \
             + ColorOptions.panels \
             + ContentOrientationOptions.panels \
             + ContentAlignmentOptions.panels \
             + ImagePositionOptions.panels \
             + OnloadContentFadeOptions.panels \
             + OnloadImageFadeOptions.panels \
             + OnscrollContentFadeOptions.panels \
             + OnscrollImageFadeOptions.panels \
             + ScreenOptions.panels

    class Meta:
        verbose_name = "Banner Styling"


@register_snippet
class SpotlightStyling(StylingBase, StyleOptions, ColorOptions, ContentOrientationOptions, ContentAlignmentOptions,
                ImagePositionOptions, OnloadContentFadeOptions, OnloadImageFadeOptions, OnscrollContentFadeOptions,
                OnscrollImageFadeOptions, ScreenOptions):
    """
        SpotlightStyling
    """
    panels = StylingBase.panels \
             + StyleOptions.panels \
             + ColorOptions.panels \
             + ContentOrientationOptions.panels \
             + ContentAlignmentOptions.panels \
             + ImagePositionOptions.panels \
             + OnloadContentFadeOptions.panels \
             + OnloadImageFadeOptions.panels \
             + OnscrollContentFadeOptions.panels \
             + OnscrollImageFadeOptions.panels \
             + ScreenOptions.panels

    class Meta:
        verbose_name = "Spotlight Styling"


@register_snippet
class GalleryStyling(StylingBase, StyleOptions, ColorOptions, SizeOptions):
    """
        Gallery Style Options
    """
    lightbox_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=32,
    )
    onload_fade_in = models.BooleanField(verbose_name="Fade In on Load", default=False)
    onscroll_fade_in = models.BooleanField(verbose_name="Fade In on Scroll", default=False)

    panels = StylingBase.panels \
             + StyleOptions.panels \
             + ColorOptions.panels \
             + SizeOptions.panels \
             + [
                FieldPanel('lightbox_button_text'),
                FieldPanel('onload_fade_in'),
                FieldPanel('onscroll_fade_in')
            ]

    class Meta:
        verbose_name = "Gallery Styling"


@register_snippet
class ItemStyling(StylingBase, StyleOptions, ColorOptions, SizeOptions):
    """
        Item Styling
    """

    onload_fade_in = models.BooleanField(verbose_name="Fade In on Load", default=False)
    onscroll_fade_in = models.BooleanField(verbose_name="Fade In on Scroll", default=False)

    panels = StylingBase.panels \
             + StyleOptions.panels \
             + ColorOptions.panels \
             + SizeOptions.panels \
             + [
                FieldPanel('onload_fade_in'),
                FieldPanel('onscroll_fade_in')
            ]

    class Meta:
        verbose_name = "Item Styling"


@register_snippet
class SectionStyling(StylingBase, ColorOptions):
    """
        Item Styling
    """

    panels = StylingBase.panels \
             + ColorOptions.panels

    class Meta:
        verbose_name = "Section Styling"


@register_snippet
class FooterStyling(StylingBase, ColorOptions):
    """
        Footer Styling
    """

    panels = StylingBase.panels \
             + ColorOptions.panels

    class Meta:
        verbose_name = "Footer Styling"


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

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('major'),
        FieldPanel('minor'),
        ImageChooserPanel('image'),
        FieldPanel('styling_options'),
        FieldPanel('actions'),
    ]

    subpage_types = []

    def get_context(self, request):
        context = super(BannerPage, self).get_context(request)
        context['banner'] = self
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
        'home.SpotlightStyling',
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
    styling_options = models.ForeignKey(
        'home.SectionStyling',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('headline', classname="full"),
        FieldPanel('introduction', classname="full"),
        FieldPanel('styling_options')
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
        blank=True
    )
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
        blank=True
    )
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
        context['gallery'] = self
        return context


class ItemPage(Page):
    """
        Item Page
    """
    icon = models.CharField(max_length=30, blank=True, default='')
    headline = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    text = models.TextField(
        blank=True)
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
        FieldPanel('icon'),
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
    styling_options = models.ForeignKey(
        'home.ItemStyling',
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


class FooterPage(Page):
    """
        Footer Page
    """
    text = RichTextField(blank=True)
    icons = models.ForeignKey(
        'home.IconButtons',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    styling_options = models.ForeignKey(
        'home.FooterStyling',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('styling_options'),
        FieldPanel('text'),
        FieldPanel('icons'),
    ]

    subpage_types = []

    def get_context(self, request):
        context = super(FooterPage, self).get_context(request)
        context['footer'] = self
        return context


class StreamPage(Page):
    """
        Home Stream Page
    """
    footer = models.ForeignKey(
        'home.FooterPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content = StreamField([
        ('banner', PageChooserBlock(target_model='home.BannerPage', null=True, blank=True)),
        ('section_index', PageChooserBlock(target_model='home.SectionIndexPage', null=True, blank=True)),
        ('gallery', PageChooserBlock(target_model='home.GalleryPage', null=True, blank=True)),
        ('item_index', PageChooserBlock(target_model='home.ItemIndexPage', null=True, blank=True)),
        ('spotlight_index', PageChooserBlock(target_model='home.SpotlightIndexPage', null=True, blank=True)),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('footer'),
        StreamFieldPanel('content'),
    ]

    subpage_types = [
        'StreamPage',
        'BannerPage',
        'SpotlightIndexPage',
        'SectionIndexPage',
        'GalleryPage',
        'ItemIndexPage'
    ]

