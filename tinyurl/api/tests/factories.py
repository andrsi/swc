import factory
from api import models


class ShortLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ShortLink
        django_get_or_create = ['slug', ]

    original_url = 'https://example.com'
    slug = 'abcde'
