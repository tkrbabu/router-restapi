from django.urls import path
from . import views

urlpatterns = [

    path('t/',views.apiOverview, name="t"),
    path('tlst/',views.routerList, name="tlst"),
    path('tinfo/<str:pk>/',views.routerinfo, name="tinfo"),
    path('tcreate/',views.routerCreate, name="tcreate"),
    path('tupdate/<str:pk>/',views.routerUpdate, name="tupdate"),
    path('tdelete/<str:pk>/',views.routerDelete, name="tdelete"),
    path('tbulk/',views.routerBulk, name="tbulk"),

]