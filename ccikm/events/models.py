from django.db import models

# Create your models here.


class Events(models.Model):
    events_title = models.CharField(
        max_length=200, verbose_name="Events Title")
    events_image = models.ImageField(
        upload_to='events_picture', verbose_name="Image")
    events_date = models.DateTimeField(auto_now_add=True)
    events_details = models.TextField(verbose_name="what is on your mind?")
    slug = models.SlugField(max_length=264, unique=True)
    events_image_caption = models.TextField(verbose_name="Image caption")

    def __str__(self):
        return self.events_title
