from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
    image = forms.ImageField(error_messages= {'required':'Image is needed'})
        