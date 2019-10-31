from management import views
from django.urls import path


urlpatterns = [ 
    path('projects/', views.get_projects, name="secure.projects"),
    path('projects/create/', views.create_project, name="secure.project.create"),
    path('projects/<int:pk>/', views.profile_project, name="secure.project.profile"),
    path('projects/<int:pk>/update/', views.update_project, name="secure.project.update"),
    path('projects/<int:pk>/delete/', views.delete_project, name="secure.project.delete"),
]
