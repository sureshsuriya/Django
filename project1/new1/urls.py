from django.urls import path
from new1 import views

urlpatterns=[
    path('',views.home1,name="home1"),
    path('home/',views.home,name = "home"),
    path('req/<pk><a>',views.req,name = "req2"),
    path('next/',views.fun,name="next1")
]