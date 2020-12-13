from django.urls import path
from . import views

urlpatterns = [
    path('your_account/', views.your_account, name='your_account'),

]
