from django.contrib import admin
import cloudinary.uploader

# Register your models here.
from .models import Artwork

admin.site.register(Artwork)


class ArtworkAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if 'image' in request.FILES:
            uploaded = cloudinary.uploader.upload(request.FILES['image'])
            obj.image = uploaded['secure_url']
        super().save_model(request, obj, form, change)