from django.urls import path
from .import views


urlpatterns = [
    path('',views.bloghome,name='bloghome'),
    path('<int:blog_id>/',views.details,name='details'),
]
