from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="img_owner.username")
    basic_thumb = serializers.SerializerMethodField("get_basic_thumb_url")
    premium_thumb = serializers.SerializerMethodField("get_premium_thumb_url")
    tier = serializers.ReadOnlyField(source="img_owner.is_basic")
    tier2 = serializers.ReadOnlyField(source="img_owner.is_premium")
    tier3 = serializers.ReadOnlyField(source="img_owner.is_enterprise")

    class Meta:
        model = Image
        fields = [
            "url",
            "author",
            "img_owner",
            "image",
            "basic_thumb",
            "premium_thumb",
            "date_added",
            "tier",
            "tier2",
            "tier3",
        ]

    def get_basic_thumb_url(self, obj):
        # Create thumbnail url and add absolute path for working link
        request = self.context.get("request")
        thumb_url = obj.basic_thumb.url
        return request.build_absolute_uri(thumb_url)

    def get_premium_thumb_url(self, obj):
        # Create thumbnail url and add absolute path for working link
        request = self.context.get("request")
        thumb_url = obj.premium_thumb.url
        return request.build_absolute_uri(thumb_url)
