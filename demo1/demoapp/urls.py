from demoapp import views
from django.urls import path

urlpatterns=[
    path('',views.log,name="login"),
    path('log1/',views.log1,name='login1'),
]