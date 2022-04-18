from django.urls import path
from User_Management.views import login, doctor_site, admin_site

app_name = 'user'

urlpatterns = [
    path('', login, name='login'),
    path('doctor_site',doctor_site, name='doctor'),
    path('admin_site',admin_site, name='admin_site'),
]