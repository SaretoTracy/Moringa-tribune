from django.db import models
from datetime import datetime as dt

# Create your models here.
class UrlDateConverter:
    regex='\d{4}-\d{2}-\d{2}'
    format='%Y-%m-%d'
    def to_python(self,value):
        return dt.strptime(value,self.format)

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()
    def delete_editor(self):
        self.delete()
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)