from django.db import models
from datetime import datetime as dt

# Create your models here.
class UrlDateConverter:
    regex='\d{4}-\d{2}-\d{2}'
    format='%Y-%m-%d'
    def to_python(self,value):
        return dt.strptime(value,self.format)