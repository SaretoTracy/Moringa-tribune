from django.urls import path,register_converter,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .models import UrlDateConverter

register_converter(UrlDateConverter,'date')

urlpatterns = [
    # path('',views.welcome,name = 'welcome'),
    path('',views.news_of_day,name='newsToday'),
    path('archives/<date:past_date>/',views.past_days_news,name = 'pastNews'),
    path (r'^search/', views.search_results, name='search_results'),
    path('article/<int:article_id>/',views.article,name ='article'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('new/article', views.new_article, name='new-article'),

]


#serve uploaded images on the development server 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)