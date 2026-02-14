from django.urls import path
from crudapp.views import *

urlpatterns = [
    path("authors",AuthorAPI.as_view()),
    path("author/<id>",AuthorUpdateAPI.as_view()),

    path("book/author/<id>",addbook,name="addbook"),
    path("book/author/<id>/<bid>",updatebook,name="updatebook"),
    path("books",viewbook,name="books"),
    path("books/<id>",BookById.as_view()),
]