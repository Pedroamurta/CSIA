from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length= 20, blank= False, unique= True)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name

class Image(models.Model):

    image = models.ImageField(blank= False, upload_to= 'gallery/static/media', error_messages='no file uploaded')
    title = models.CharField(max_length= 40, blank= False, unique= True, error_messages='no title detected')
    tags = models.ManyToManyField(Tag, blank= True, error_messages= 'someting wrong with the tags')

    def __str__(self):
        return self.title
