
from django.urls import path,include
from . import views

app_name="Staff"

urlpatterns = [
path('', views.home, name='home'),
path('profile',views.profile, name='profile'),
path('Assign',views.Assign, name='Assign'),
path('Assign1/<int:id>',views.Assign1, name='Assign1'),
path('deleteplan',views.deleteplan, name='deleteplan'),
path('saveplan',views.saveplan, name='saveplan'),
path('SubmitCase/<int:id>',views.SubmitCase, name='SubmitCase'),
path('SubmitCase1/<int:id>',views.SubmitCase1, name='SubmitCase1'),
path('finished',views.finished, name='finished'),
]
