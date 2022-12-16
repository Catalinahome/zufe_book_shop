from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    blist = get_all_book()
    btime = get_book_by_time()
    return render(request, "book/index.html", {"blist1": blist[:10], "blist2": btime[:10]})


def search(request):
    bname = request.POST.get('name')
    blist = search_book(bname)
    return render(request, "book/book_search.html", {"blist1": blist})