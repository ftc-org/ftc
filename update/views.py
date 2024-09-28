from django.shortcuts import render, get_object_or_404
from django.db.models import OuterRef, Subquery
from update.models import Event, Update


def event_list(request):
    # events = Event.objects.filter(is_live=True).order_by("-created_at").prefetch_related("updates")
    events = Event.objects.annotate(
        latest_update=Subquery(
            Update.objects.filter(event=OuterRef('pk'))
            .order_by('-created_at')
            .values('created_at')[:1]
        )
    ).order_by('-latest_update').prefetch_related("updates")
    live_events = events.filter(is_live=True)
    latest_event = live_events.first()
    return render(request, "update/event_list.html", {"events": events, "live_events": live_events, "latest_event": latest_event})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    related_events = Event.objects.exclude(id=event.id)[:5]
    return render(
        request, "update/event_detail.html", {"event": event, "related_events": related_events}
    )

