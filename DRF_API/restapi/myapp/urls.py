from django.urls import path 
from myapp.views import *

urlpatterns =[
    path("get-api",get_api,name="get_api"),
    path("post-api",post_api,name="post_api"),
    path("put-api",put_api,name="put_api"),
    path("delete-api",delete_api,name="delete_api"),

    path("students",students,name="students"),
    path("add-students",add_students,name="add_students"),
    path("update-students/<id>",update_students,name="update_students"),
    path("delete-students/<id>",delete_students,name="delete_students"),
]