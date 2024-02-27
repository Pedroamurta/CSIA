from django import forms
from .models import Image, Tag

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
    image = forms.ImageField(error_messages= {'required':'Image is needed'})
    title = forms.CharField(max_length=20)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'