from django.urls import path, include
# from app1.views import index
from app1.views import *  #all ifiles import


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
]

# # Error handling
# handler404='app1.views.custom_404'