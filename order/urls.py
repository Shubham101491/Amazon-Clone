from django.urls import path
from . import views

urlpatterns = [
    path('return_order/', views.return_order, name='return_order'),
    path('cancelled_order/', views.cancelled_order, name='cancelled_order'),
    path('open_order/', views.open_order, name='open_order'),
    path('buy_again/', views.buy_again, name='buy_again'),

]
