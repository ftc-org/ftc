from django.shortcuts import render, get_object_or_404
from update.models import Event


def event_list(request):
    events = Event.objects.filter(is_live=True).order_by("-updated_at").prefetch_related("updates")
    return render(request, "update/event_list.html", {"events": events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    updates = event.updates.all().order_by("-created_at")
    return render(
        request, "update/event_detail.html", {"event": event, "updates": updates}
    )
