from rest_framework import serializers

from update.models import Event, EventImage, Post, Update, UpdateImage


class UpdateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateImage
        fields = ["image", "caption"]


class UpdateSerializer(serializers.ModelSerializer):
    images = UpdateImageSerializer(many=True, read_only=True)

    class Meta:
        model = Update
        fields = [
            "id",
            "summary",
            "images",
            "content",
            "author",
            "created_at",
            "updated_at",
        ]


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ["image", "caption"]


class EventSerializer(serializers.ModelSerializer):
    updates = UpdateSerializer(many=True, read_only=True)
    updated_at = serializers.SerializerMethodField()
    image = EventImageSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
            "author",
            "is_live",
            "updates",
            "image",
        ]

    def get_updated_at(self, obj):
        if hasattr(obj, "latest_update") and obj.latest_update:
            return obj.latest_update
        return obj.updated_at


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
            "created_at",
            "updated_at",
            "image",
        ]
