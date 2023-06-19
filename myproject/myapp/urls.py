from django.urls import path
from . import views
urlpatterns = [
    path("items/", views.index, name="index"),
    path('create/',views.create,name='create'),
    path('upload/<int:id>',views.upload,name='upload'),
    
]