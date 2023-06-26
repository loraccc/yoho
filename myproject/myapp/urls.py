from django.urls import path,include
from . import views
from .views import *
urlpatterns = [
    path("index/", views.index, name="index"),
    path('create/',views.create,name='create'),
    path('upload/<int:id>',views.upload,name='upload'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('upload/',views.upload,name='upload'),
    
    path('persons/', PersonList.as_view(), name='person-list'),
    path('persons/<int:pk>/', PersonDetail.as_view(), name='person-detail'),
    
    
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    
    
]