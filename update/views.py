from django.shortcuts import render, get_object_or_404
from update.models import Event


def event_list(request):
    event = Event.objects.latest("-updated_at")
    updates = event.updates.all()
    return render(request, "update/event_list.html", {"event": event, "updates": updates})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    updates = event.updates.all()
    return render(
        request, "update/event_detail.html", {"event": event, "updates": updates}
    )
