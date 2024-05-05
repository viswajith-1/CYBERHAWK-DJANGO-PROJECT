
from django.urls import path,include
from . import views

app_name="Manager"

urlpatterns = [
path('', views.home, name='home'),
path('profile',views.profile, name='profile'),
path('CaseStatus',views.CaseStatus, name='CaseStatus'),
path('CaseStatus2/<int:id>',views.CaseStatus2, name='CaseStatus2'),
path('SubmitCase/<int:id>',views.SubmitCase, name='SubmitCase'),
path('CancelCase/<int:id>',views.CancelCase, name='CancelCase'),
path('ViewEmployees',views.ViewEmployees, name='ViewEmployees'),
path('Assign',views.Assign, name='Assign'),
path('Assign1/<int:id>',views.Assign1, name='Assign1'),
path('Assign2/<int:id>',views.Assign2, name='Assign2'),

path('Finished',views.Finished, name='Finished'),
path('Finished2/<int:id>',views.Finished2, name='Finished2'),
]

