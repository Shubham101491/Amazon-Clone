from django.urls import path
from . import views

urlpatterns = [
    path('your_account/', views.your_account, name='your_account'),
    path('your_addresses/', views.your_addresses, name='your_addresses'),
    path('new_address/', views.new_address, name='new_address'),

]
