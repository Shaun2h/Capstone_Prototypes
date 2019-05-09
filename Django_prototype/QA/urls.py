from django.urls import path
from . import views
urlpatterns = [
    path("", views.basic, name="Default"),
    path("template1", views.test1),
    path("template2", views.test2),
    path("template3", views.test3),
    path("insert", views.insert_req, name="Default"),
    path("delete", views.del_req, name="Default"),
               ]
# where names is how you prefer to call this method. Dictates the method called in views.py in this
# module.
