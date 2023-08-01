from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload,name='upload_data'),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    path('compute/', views.compute_data, name='compute_data'),
    path('plot/', views.plot, name='plot')  
]
