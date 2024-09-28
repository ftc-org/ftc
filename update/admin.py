from django.contrib import admin
from update.models import Event, Update, UpdateImage, EventImage

# Register your models here.
admin.site.register(Event)
admin.site.register(Update)
admin.site.register(UpdateImage)
admin.site.register(EventImage)

