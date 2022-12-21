from django.shortcuts import render


# index应用的视图函数
def index(request):
    return render(request, 'index/index.html')
