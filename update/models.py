from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_live = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="image", null=True)
    image = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption

class Update(models.Model):
    event = models.ForeignKey(Event, related_name='updates', on_delete=models.CASCADE)
    summary = models.CharField(max_length=200, default="")
    content = models.TextField()
    content = models.TextField(default="", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.event.title} - {self.summary}"

    def time_since(self):
        now = timezone.now()
        diff = now - self.created_at

        if diff.days > 0:
            return f"{diff.days}d ago"
        elif diff.seconds >= 3600:
            return f"{diff.seconds // 3600}h ago"
        elif diff.seconds >= 60:
            return f"{diff.seconds // 60}m ago"
        else:
            return "Just now"

class UpdateImage(models.Model):
    update = models.ForeignKey(Update, related_name="images", on_delete=models.CASCADE, null=True)
    caption = models.CharField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

