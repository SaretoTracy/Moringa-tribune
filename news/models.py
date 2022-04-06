from django.db import models
from tinymce.models import HTMLField
import datetime as dt
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UrlDateConverter:
    regex='\d{4}-\d{2}-\d{2}'
    format='%Y-%m-%d'
    def to_python(self,value):
        return dt.datetime.strptime(value,self.format)


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length =60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/',default="")

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news



    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    @classmethod
    def search_by_tags(cls, tags):
        image= cls.objects.filter(tags__tags__icontains=tags)
        return image

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
