from rest_framework import serializers
from api import models


class ShortLinkSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(read_only=True)

    class Meta:
        fields = [
            'original_url',
            'short_url',
        ]
        model = models.ShortLink
