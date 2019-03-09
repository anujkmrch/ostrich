from django.urls import path

from . import views

urlpatterns = [
    # ex: get-light-status-from-qr/y19SVa112kjx
    path('by-qr/<char:id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('getVehicleDensity', views.results, name='results'),
]