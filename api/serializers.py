from rest_framework.serializers import ModelSerializer

from update.models import Event, Update

class UpdateSerializer(ModelSerializer):
    class Meta:
        model = Update
        fields = [
            "summary",
            "content",
            "author",
            "created_at",
            "updated_at"
        ]

class EventSerializer(ModelSerializer):
    updates = UpdateSerializer(many=True, read_only=True)
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
        ]


