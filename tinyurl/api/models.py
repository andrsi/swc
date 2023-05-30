import random
import string

from django.conf import settings
from django.db import models
from django.utils.functional import cached_property


class ShortLink(models.Model):
    original_url = models.URLField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    objects = models.Manager()

    @cached_property
    def short_url(self):
        return f'{settings.BASE_URL}/{self.slug}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.generate_random_slug()
        super().save()

    @classmethod
    def generate_random_slug(cls):
        letters = string.ascii_lowercase
        slug = ''.join(random.choice(letters) for i in range(settings.LENGTH_SLUG))
        if not cls.objects.filter(slug=slug).exists():
            return slug
        else:
            cls.generate_random_slug()
