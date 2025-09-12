from django.shortcuts import render
from .models import *

def index_view(request):
    context = {
        'about':About.objects.first(),
        'images':Images.objects.first(),
        'text':Text.objects.first(),
    }
    return render(request,"index.html",context)
