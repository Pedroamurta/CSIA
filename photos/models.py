from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length= 20, blank= False, unique= True)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name

class Image(models.Model):

    image = models.ImageField(blank= False, upload_to= 'gallery/static/media')
    title = models.CharField(max_length= 40, blank= False, unique= True)
    tags = models.ManyToManyField(Tag, blank= True)

    def __str__(self):
        return self.title
