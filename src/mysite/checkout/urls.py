from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('additem', views.additem, name='additem'),
    path('database_opt', views.database_opt, name='database_opt')
]