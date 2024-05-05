
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import Settings, settings
urlpatterns = [
    path("admin/", admin.site.urls),
    
     path('',include('Guest.urls')),
    path('Admin/',include('Admin.urls')),
    path('Manager/',include('Manager.urls')),
    path('Staff/',include('Staff.urls')),
    path('User/',include('User.urls'))   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
