from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from base.blocks import BaseStreamBlock


class HomePage(Page):
    pass


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


    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('content'),
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





