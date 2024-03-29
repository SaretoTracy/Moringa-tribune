from django.http  import HttpResponse
import datetime as dt
from .forms import NewArticleForm, NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist
from .models import Article,NewsLetterRecipients
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  MoringaMerch
from .serializer import MerchSerializer
from .permissions import IsAuthenticatedOrReadOnly


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def news_of_day(request):
    # Function that gets the date
    date = dt.date.today()
     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    news = Article.todays_news()
    form = NewsLetterForm()


    return render(request, 'all-news/today-news.html',{"date": date, "news": news, "letterForm":form})

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_news(request,past_date):
    try:
        # Converts data from the string Url
        date =  past_date
        day = convert_dates(past_date)
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_of_day)
    news= Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news": news})
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_tags(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})

#.....
@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('newsToday')

    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})

class MerchList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


       