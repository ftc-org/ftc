from django.contrib import admin
from .models import Event, EventImage, Update, UpdateImage, Post
from django.utils import timezone


class EventImageInline(admin.StackedInline):
    model = EventImage
    extra = 1


class UpdateInline(admin.TabularInline):
    model = Update
    extra = 1
    fields = ("summary", "content", "author", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_live", "created_at", "updated_at")
    list_filter = ("is_live", "author")
    search_fields = ("title", "description")
    inlines = [EventImageInline, UpdateInline]
    fieldsets = (
        (None, {"fields": ("title", "description", "author", "is_live")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
    readonly_fields = ("created_at", "updated_at")


class UpdateImageInline(admin.TabularInline):
    model = UpdateImage
    extra = 1


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ("event", "summary", "author", "created_at", "time_since")
    list_filter = ("event", "author")
    search_fields = ("summary", "content")
    inlines = [UpdateImageInline]
    readonly_fields = ("created_at", "updated_at", "time_since")

    def time_since(self, obj):
        if obj.created_at:
            now = timezone.now()
            diff = now - obj.created_at
            if diff.days > 0:
                return f"{diff.days}d ago"
            elif diff.seconds >= 3600:
                return f"{diff.seconds // 3600}h ago"
            elif diff.seconds >= 60:
                return f"{diff.seconds // 60}m ago"
            else:
                return "Just now"
        return "Not created yet"

    time_since.short_description = "Time Since Creation"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "created_at", "updated_at")
    list_filter = ("is_published", "author")
    search_fields = ("title", "content")
    fieldsets = (
        (None, {"fields": ("title", "content", "author", "is_published", "image")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
    readonly_fields = ("created_at", "updated_at")


admin.site.site_header = "FTC Content Management Admin"
admin.site.site_title = "FTC Content Management Portal"
admin.site.index_title = "Welcome to FTC Content Management Portal"
