from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import io
from prose.fields import RichTextField


class OptimizedImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        self.max_size = kwargs.pop("max_size", (1920, 1080))
        self.quality = kwargs.pop("quality", 85)
        super(OptimizedImageField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        file = super(OptimizedImageField, self).pre_save(model_instance, add)

        if file and isinstance(file, InMemoryUploadedFile):
            image = Image.open(file)
            image_format = image.format.lower()

            # Resize image
            image.thumbnail(self.max_size, Image.LANCZOS)

            # Save the image to a BytesIO object
            output = io.BytesIO()

            # Apply compression for JPEG and PNG images
            if image_format in ("jpeg", "jpg"):
                image.save(output, format="JPEG", quality=self.quality, optimize=True)
            elif image_format == "png":
                image.save(output, format="PNG", optimize=True)
            else:
                image.save(output, format=image_format)

            output.seek(0)

            # Replace the file on the model
            file_name = file.name.split("/")[-1]
            content = ContentFile(output.read())
            file.save(file_name, content, save=False)

        return file


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_live = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.OneToOneField(
        Event, on_delete=models.CASCADE, related_name="image", null=True
    )
    image = OptimizedImageField(null=True, blank=True)
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption


class Update(models.Model):
    event = models.ForeignKey(Event, related_name="updates", on_delete=models.CASCADE)
    summary = models.CharField(max_length=200, default="")
    content = RichTextField(default="", blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.event.title} - {self.summary}"


class UpdateImage(models.Model):
    update = models.ForeignKey(
        Update, related_name="images", on_delete=models.CASCADE, null=True
    )
    caption = models.CharField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    image = OptimizedImageField(null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, default="")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = OptimizedImageField(null=True, blank=True)

    def __str__(self):
        return self.title
