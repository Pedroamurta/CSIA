from django.shortcuts import render
from .forms import ImageForm, TagForm
from .models import Image, Tag

# Create your views here.
def home_view(request):
    tags = Tag.objects.all()
    return render(request, 'home.html', {'tags':tags})

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
        psearch = request.POST.getlist('psearch')
        images = Image.objects.filter(tags__name__in= psearch).distinct()
        return render(request, 'search.html', {'psearch':psearch,
                                               'images': images})
    else:
        return render(request, 'search.html', {})
    
def tag_view(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tag.html',{'form':form})