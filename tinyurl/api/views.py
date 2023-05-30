from rest_framework import mixins, viewsets

from api import serializers, models


class ShortLinkViewSet(mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    http_method_names = ['post', 'get', 'head']
    serializer_class = serializers.ShortLinkSerializer
    lookup_field = 'slug'
    queryset = models.ShortLink.objects.all()
