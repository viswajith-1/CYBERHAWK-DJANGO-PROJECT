
from django.urls import path,include
from . import views

app_name="User"

urlpatterns = [
path('', views.home, name='home'),
path('registercase', views.registercase, name='registercase'),
path('newsUpdates',views.newsUpdates, name='newsUpdates'),
path('profile',views.profile, name='profile'),
path('caseviewmore',views.caseviewmore, name='caseviewmore'),
path('view_case/<int:id>',views.view_case, name='view_case'),
path('SubmitCase/<int:id>',views.SubmitCase, name='SubmitCase'),
path('CancelCase/<int:id>',views.CancelCase, name='CancelCase'),
]
