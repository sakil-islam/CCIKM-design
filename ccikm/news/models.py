from django.db import models

# Create your models here.


class News(models.Model):
    news_title = models.CharField(max_length=200, verbose_name="News Title")
    news_image = models.ImageField(
        upload_to='news_picture', verbose_name="Image")
    news_date = models.DateTimeField(auto_now_add=True)
    news_details = models.TextField(verbose_name="what is on your mind?")
    slug = models.SlugField(max_length=264, unique=True)
    news_image_caption = models.TextField(verbose_name="Image caption")

    def __str__(self):
        return self.news_title
