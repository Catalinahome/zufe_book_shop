from django.shortcuts import render


# news应用的视图函数
def index(request):
    return render(request, 'news/news.html')