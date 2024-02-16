from django.shortcuts import render, redirect,get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def main_view(request):  
    return render(request,"main.html",{})  
