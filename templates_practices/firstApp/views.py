from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
         return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
        context={'a':1, 'b':2,  'genres':['Fiction', 'Non-Fiction', 'Science Fiction', 'Mystery'],   'special_book' :{
        'title': 'The Special Book',
        'author': 'Special Author',
        'publication_year': 2022,
    }}
        return render(request, 'index.html', context)
