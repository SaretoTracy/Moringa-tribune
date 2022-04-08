
from django.contrib import admin
from .models import Article,tags,MoringaMerch
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)# filter_horizontal property that allows ordering of many to many fields
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
admin.site.register(MoringaMerch)