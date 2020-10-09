from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects),
    path('gallery/', views.gallery),
    path('advisors/', views.our_team),
    path('projects/<int:project_id>/', views.projects_details, name='project-detail'),
    # re_path(r'projects?/<int:projects_id>', views.projects_details),
]
