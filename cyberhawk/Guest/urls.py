
from django.urls import path,include
from . import views

app_name="Guest"

urlpatterns = [
path('', views.home, name='home'),
path('Login',views.Login, name='Login'),
path('UserRegister',views.UserRegister, name='UserRegister'),
path('newsUpdates',views.newsUpdates, name='newsUpdates'),
path('deleteplan',views.deleteplan, name='deleteplan'),
path('saveplan',views.saveplan, name='saveplan'),
path('faq',views.faq, name='faq'),
path('contactus',views.contactus, name='contactus'),
path('generallearningcorner',views.generallearningcorner, name='generallearningcorner'),
]
