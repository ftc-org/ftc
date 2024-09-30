from rest_framework.serializers import ModelSerializer

from update.models import Event, EventImage, Post, Update, UpdateImage


class UpdateImageSerializer(ModelSerializer):
    class Meta:
        model = UpdateImage
        fields = ["image", "caption"]


class UpdateSerializer(ModelSerializer):
    images = UpdateImageSerializer(many=True, read_only=True)

    class Meta:
        model = Update
        fields = ["summary", "images", "content", "author", "created_at", "updated_at"]


class EventImageSerializer(ModelSerializer):
    class Meta:
        model = EventImage
        fields = ["image", "caption"]


class EventSerializer(ModelSerializer):
    updates = UpdateSerializer(many=True, read_only=True)
    image = EventImageSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "created_at",
            "updated_at",
            "author",
            "is_live",
            "updates",
            "image",
        ]

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "author", "created_at", "updated_at", "image"] 
