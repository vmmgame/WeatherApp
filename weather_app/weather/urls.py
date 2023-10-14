from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('results', views.results_page, name='results-page')
]
