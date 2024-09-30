from rest_framework.mixins import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from api.serializers import EventSerializer, PostSerializer
from django.db.models import OuterRef, Prefetch, Subquery
from update.models import Event, Update, Post
from django_filters.rest_framework import DjangoFilterBackend


class EventViewSet(ReadOnlyModelViewSet):
    queryset = (
        Event.objects.annotate(
            latest_update=Subquery(
                Update.objects.filter(event=OuterRef("pk"))
                .order_by("-created_at")
                .values("created_at")[:1]
            )
        )
        .order_by("-latest_update")
        .prefetch_related(
            Prefetch("updates", queryset=Update.objects.prefetch_related("images"))
        )
    )
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "is_live"]

    @action(detail=True, methods=["GET"])
    def related(self, request, pk=None):
        event = self.get_object()
        related_events = Event.objects.exclude(id=event.id)
        page = self.paginate_queryset(related_events)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(related_events, many=True)
        return Response(serializer.data)


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "author"]
