from django.urls import path
from .views import *

urlpatterns = [
    path("",index_view),
    path('album/', category_list, name='category_list'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
]
