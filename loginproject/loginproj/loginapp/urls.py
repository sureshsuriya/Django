from loginapp import views
from django.urls import path

urlpatterns=[
    path('',views.login,name="login"),
    path('log1/',views.log1,name='login1'),
    path('log2/<s>',views.log2,name='login2'),
]

