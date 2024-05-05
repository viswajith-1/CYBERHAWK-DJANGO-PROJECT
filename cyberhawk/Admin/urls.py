
from django.urls import path,include
from . import views

app_name="Admin"

urlpatterns = [
path('', views.home, name='home'),

path('viewmanager', views.viewmanager, name='viewmanager'),
path('viewstaff', views.viewstaff, name='viewstaff'),
path('viewusers', views.viewusers, name='viewusers'),

path('post', views.add_post, name='post'),
path('add', views.add, name='add'),
path('profile', views.profile, name='profile'),

path('statastics', views.statastics, name='statastics'),

path('CaseStatus', views.CaseStatus, name='CaseStatus'),
path('CaseStatus2/<int:id>', views.CaseStatus2, name='CaseStatus2'),
path('SubmitCase/<int:id>', views.SubmitCase, name='SubmitCase'),
path('CancelCase/<int:id>', views.CancelCase, name='CancelCase'),
]
