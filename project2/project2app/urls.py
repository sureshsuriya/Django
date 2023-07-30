from django.urls import path
from project2app import views
urlpatterns=[
    path('',views.login,name="logi"),
    path('log2/<s><r>',views.log2,name="login2"),
    path('age/<s>',views.age,name="age"),
    path('subm/<w>',views.subm,name="age1"),
    path('subm1/<ag>',views.subm1,name="age2"),
    path('add/',views.ad,name="addnum"),
    path('test/<a>',views.test,name="res"),
    path('demo/',views.hom,name="Home"),
    path('hom2/<a><d><r><e><w>',views.hom2,name="Hom2")

]