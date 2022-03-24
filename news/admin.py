
from django.contrib import admin
from .models import Editor,Article,tags
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)# filter_horizontal property that allows ordering of many to many fields
admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)