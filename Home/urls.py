
from django.contrib import admin
from django.urls import path
from . import views

app_name= "Home"
urlpatterns = [
   
    path("",views.index, name="home_page" ),
    path("record/create/", views.RecordAddView.as_view() ,name="create_record"),
    path("record/multiple/", views.UploadMutiple.as_view(), name ="uploadfile"),
    path("records/", views.ListFiles.as_view(), name="listview")
]
