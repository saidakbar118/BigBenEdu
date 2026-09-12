from django.urls import path

from .views import (
    index_view,
    category_list,
    category_detail,
)


urlpatterns = [

    path(
        "",
        index_view,
        name="index"
    ),

    path(
        "album/",
        category_list,
        name="category_list"
    ),

    path(
        "category/<int:pk>/",
        category_detail,
        name="category_detail"
    ),

]