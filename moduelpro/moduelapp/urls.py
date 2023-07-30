from django.urls import path
from moduelapp import views
urlpatterns=[
    path('login/', views.login, name='login'),
    # Add other URL patterns if needed
    path('na',views.mod,name="moduel"),
    path('model/<w>',views.mod2,name="moduel2")
]