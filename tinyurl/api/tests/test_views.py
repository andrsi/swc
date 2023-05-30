import json

from django.conf import settings
from django.test import TestCase

from api import models
from api.tests import factories


class ShortLinkTestCase(TestCase):
    URL = '/api/shortlink/'

    def test__retrieve__returns_correct_data(self):
        short_link_1 = factories.ShortLinkFactory.create(original_url='https://example.com/a', slug='abcde')

        response = self.client.get(self.URL + f'{short_link_1.slug}/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content['original_url'], 'https://example.com/a')

    def test__create__returns_correct_data(self):
        response = self.client.post(self.URL, data={'original_url': 'https://example.com/something'})
        self.assertEqual(response.status_code, 201)
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content['original_url'], 'https://example.com/something')
        self.assertRegex(content['short_url'], f'^{settings.BASE_URL}/[\w+]')
        self.assertEqual(models.ShortLink.objects.count(), 1)
