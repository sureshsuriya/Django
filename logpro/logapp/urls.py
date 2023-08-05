from django.urls import path
from logapp import views
urlpatterns=[
    path('gf/',views.imag,name='nam'),
    path('gk/',views.war,name='war1'),
    path('',views.log,name='log'),
    # path('log1/',views.log2,name='log2')
]