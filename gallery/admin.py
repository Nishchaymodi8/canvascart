from django import forms
from django.contrib import admin
from .models import Artwork
import cloudinary.uploader

class ArtworkForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = Artwork
        fields = '__all__'


class ArtworkAdmin(admin.ModelAdmin):
    form = ArtworkForm

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('image_file'):
            uploaded = cloudinary.uploader.upload(form.cleaned_data['image_file'])
            obj.image = uploaded['secure_url']
        super().save_model(request, obj, form, change)


admin.site.register(Artwork, ArtworkAdmin)