from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})

def gallery_view(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

def create_view(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'create.html', {'form':form})

def search_view(request):
    if request.method == 'POST':
        psearch = request.POST['psearch']
        images = Image.objects.filter(tags__name= psearch)
        return render(request, 'search.html', {'psearch':psearch,
                                               'images': images})
    else:
        return render(request, 'search.html', {})