from django import forms
from django.contrib import admin
from .models import Artwork
import cloudinary.uploader


class ArtworkForm(forms.ModelForm):
    image = forms.ImageField(required=True)  # 🔥 THIS LINE IS KEY

    class Meta:
        model = Artwork
        fields = '__all__'


class ArtworkAdmin(admin.ModelAdmin):
    form = ArtworkForm

    def save_model(self, request, obj, form, change):
        image_file = form.cleaned_data.get('image')

        if image_file:
            uploaded = cloudinary.uploader.upload(image_file)
            obj.image = uploaded['secure_url']  # save URL

        super().save_model(request, obj, form, change)


admin.site.register(Artwork, ArtworkAdmin)