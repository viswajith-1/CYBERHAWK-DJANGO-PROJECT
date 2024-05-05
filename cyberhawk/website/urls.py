from django.urls import path
from . import views

urlpatterns = [
    path('', views.generalhome, name='genralhome'),
    path('generallogin',views.generallogin, name= 'generallogin'),
    path('logout',views.logout_user, name= 'logout'),
    path('generalhome', views.generalhome, name='generalhome'),
    path('generallearningcorner', views.generallearningcorner, name='generallearningcorner'),
    path('generalcontactus', views.generalcontactus, name='generalcontactus'),
    path('generalfaq', views.generalfaq, name='generalfaq'),
    path('generalpost', views.generalpost, name='generalpost'),
    path('generalregister', views.generalregister, name='generalregister'),
    path('adminregisteraccount', views.adminregisteraccount, name='adminregisteraccount'),
    path('adminpost', views.adminpost, name='adminpost'),
    path('registercase', views.registercase, name='registercase')

]