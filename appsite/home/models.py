from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from base.blocks import BaseStreamBlock

from home.sitedefaults import style_choices, orientation_choices, content_align_choices, image_position_choices, \
    onload_fade_choices, onscroll_fade_choices, color_choices


@register_snippet
class SpotlightOptions(models.Model):
    """"""

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


class HomePage(Page):

    section_1_headline = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    section_1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Featured section 1'
    )

    content_panels = Page.content_panels + [
        FieldPanel('section_1_headline'),
        PageChooserPanel('section_1'),
    ]

    subpage_types = ['SpotlightIndexPage']

    def __str__(self):
        return self.headline


class SpotlightPage(Page):
    """ """

    content = StreamField(
        BaseStreamBlock(), verbose_name="Page Content", blank=True
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    options = models.ForeignKey(
        'home.SpotlightOptions',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('content'),
        FieldPanel('options'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['SpotlightIndexPage']


class SpotlightIndexPage(Page):
    """ """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
    ]

    parent_page_types = ['HomePage']
    subpage_types = ['SpotlightPage']

    def get_spotlights(self):
        return SpotlightPage.objects.live().descendant_of(self).order_by('-first_published_at')

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
        return context



