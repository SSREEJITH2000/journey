from django.urls import path
from . import views
urlpatterns = [

    path('',views.blast,name='blast'),
    path('reg',views.register,name='register')
]