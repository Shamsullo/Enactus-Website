from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('projects/', views.render_projects),
    # path('about/', views.about)
]
