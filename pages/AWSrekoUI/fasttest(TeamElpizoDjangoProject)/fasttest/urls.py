
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
import subprocess

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', views.aboutus, name='About_Us'),
    path('', views.home, name='FrontHome'),
    path('manning365/', views.manning365, name='Manning365'),
    path('solutions/', views.solutions, name='Solutions'),
    path('aboutus/', include ('aboutus.urls')),
    path('upload/', views.upload, name='upload'),
    path('results/<nm1>/<nm2>/', views.website, name='results'),
    path('customlabel/<pc>/', views.customlabel, name='customlabel')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
