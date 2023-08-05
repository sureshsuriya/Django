from django.urls import path
from moduelapp import views
urlpatterns=[
    path('login/', views.login, name='login'),
    # Add other URL patterns if needed
    path('',views.test,name="tst"),
    path('tst1/',views.test1,name="tst2"),
    path('mod/',views.mod,name="moduel"),
    path('model/',views.mod2,name="moduel2")
]