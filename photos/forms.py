from django.forms import ModelForm, widgets
from .models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        