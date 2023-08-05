from django.urls import path
from loginapp import views
urlpatterns=[
    path('',views.log,name='log'),
    path('log1/',views.log2,name='log2')
]