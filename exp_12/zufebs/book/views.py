from django.shortcuts import render
from .models import *


# 返回book表前10的书籍信息渲染书城前端页面
def index(request):
    blist = get_all_book()
    btime = get_book_by_time()
    return render(request, "book/index.html", {"blist1": blist[:10], "blist2": btime[:10]})


# 返回书籍查询信息渲染前端查询页面
def search(request):
    bname = request.POST.get('name')
    blist = search_book(bname)
    return render(request, "book/book_search.html", {"blist1": blist})
