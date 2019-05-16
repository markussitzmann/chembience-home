from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, PageChooserPanel, InlinePanel
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import StreamField, RichTextField

from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from base.blocks import BaseStreamBlock

from home.sitedefaults import style_choices, orientation_choices, content_align_choices, image_position_choices, \
    onload_fade_choices, onscroll_fade_choices, color_choices


@register_snippet
class ActionButton(models.Model):

    SIZE_CHOICES = (
        ('', 'Default'),
        ('small', 'Small'),
        ('large', 'Large'),
    )

    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, default='')
    size = models.CharField(max_length=25, choices=SIZE_CHOICES, blank=True, default='')
    icon = models.CharField(max_length=25, blank=True, default='')

    panels = [
        FieldPanel('name'),
        FieldPanel('size'),
        FieldPanel('url'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        button_string = self.name + " (" + self.url + ")"
        if self.size:
            button_string = button_string + ", " + self.size
        return button_string


@register_snippet
class ActionButtonGroup(ClusterableModel, models.Model):

    name = models.CharField(max_length=255)
    small = models.BooleanField(verbose_name="Small Buttons", default=False)
    stacked = models.BooleanField(verbose_name="Stacked Buttons", default=False)

    panels = [
        FieldPanel('name'),
        FieldPanel('small'),
        FieldPanel('stacked'),
        InlinePanel('actions', label="Actions"),
    ]

    def __str__(self):
        return self.name


class ActionButtonGroupMember(Orderable, models.Model):

    group = ParentalKey('home.ActionButtonGroup', on_delete=models.CASCADE, related_name='actions')
    button = models.ForeignKey('home.ActionButton', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "action button group"

    panels = [
        SnippetChooserPanel('button'),
    ]

    def __str__(self):
        return self.group.name + " -> " + self.button.name



@register_snippet
class StyleOptions(models.Model):
    """

    """
    name = models.CharField(
        max_length=25,
        primary_key=True,
        default="Spotlight1"
    )
    style = models.CharField(
        max_length=25,
        choices=style_choices,
        default="No. 1"
    )
    orientation = models.CharField(
        max_length=25,
        choices=orientation_choices,
        default="orient-right"
    )
    content_align = models.CharField(
        max_length=25,
        choices=content_align_choices,
        default="content-align-left",
        null=True,
        blank=True
    )
    color = models.CharField(
        max_length=25,
        choices=color_choices,
        default="color0",
        null=True, blank=True
    )
    image_position = models.CharField(
        max_length=25,
        choices=image_position_choices,
        null=True,
        blank=True
    )
    onload_fade = models.CharField(
        max_length=25,
        choices=onload_fade_choices,
        null=True,
        blank=True
    )
    onscroll_fade = models.CharField(
        max_length=25,
        choices=onscroll_fade_choices,
        null=True,
        blank=True
    )
    color_choices = models.CharField(
        max_length=25,
        choices=color_choices,
        null=True,
        blank=True
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('style'),
        FieldPanel('orientation'),
        FieldPanel('color'),
        FieldPanel('content_align'),
        FieldPanel('image_position'),
        FieldPanel('onload_fade'),
        FieldPanel('onscroll_fade'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Spotlight options"


class BannerPage(Page):
    """
        Banner Page
    """
    header = models.CharField(max_length=127)
    major = RichTextField(verbose_name="Major Text", blank=True)
    minor = RichTextField(verbose_name="Minor Text", blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    options = models.ForeignKey(
        'home.StyleOptions',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    button_group = models.ForeignKey(
        'home.ActionButtonGroup',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('major'),
        FieldPanel('minor'),
        ImageChooserPanel('image'),
        FieldPanel('options'),
        FieldPanel('button_group'),
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
    options = models.ForeignKey(
        'home.StyleOptions',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('content'),
        FieldPanel('options'),
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
        SPotlight Index Page
    """
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
    ]

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

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('text'),
        ImageChooserPanel('image')
    ]

    search_fields = Page.search_fields + [
        index.SearchField('text'),
    ]

    parent_page_types = ['GalleryIndexPage']
    subpage_types = []

    def get_context(self, request):
        context = super(GalleryArticlePage, self).get_context(request)
        context['gallery_article'] = self
        return context


class GalleryIndexPage(Page):
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

    content_panels = Page.content_panels + [
        FieldPanel('headline', classname="full"),
        FieldPanel('introduction', classname="full"),
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
        context = super(GalleryIndexPage, self).get_context(request)
        articles = self.paginate(request, self.get_articles())
        context['articles'] = articles
        context['gallery_index'] = self
        return context


class ItemPage(Page):
    """
        Item Page
    """
    headline = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    text = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('text'),
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

    parent_page_types = []
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


class HomeStreamPage(Page):
    """
        Home Stream Page
    """
    content = StreamField([
        ('banner', PageChooserBlock(target_model='home.BannerPage', null=True, blank=True)),
        ('section_index', PageChooserBlock(target_model='home.SectionIndexPage', null=True, blank=True)),
        ('gallery_index', PageChooserBlock(target_model='home.GalleryIndexPage',null=True, blank=True)),
        ('item_index', PageChooserBlock(target_model='home.ItemIndexPage', null=True, blank=True)),
        ('spotlight_index', PageChooserBlock(target_model='home.SpotlightIndexPage', null=True, blank=True)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]
