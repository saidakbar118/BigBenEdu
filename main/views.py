from django.shortcuts import render,get_object_or_404
from .models import *

def index_view(request):
    context = {
        'about':About.objects.first(),
        'images':Images.objects.first(),
        'text':Text.objects.first(),
    }
    return render(request,"index.html",context)



def category_list(request):
    categories = Category.objects.all()
    return render(request, 'album.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    photos = category.photos.all()
    return render(request, 'photo_album.html', {'category': category, 'photos': photos})


