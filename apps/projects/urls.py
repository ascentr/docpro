from django.urls import path
from . import views

urlpatterns = [
  path('', views.ProjectListView.as_view(), name='projects'),
  path('completed/', views.completed_projects, name="completed"),
  path('ongoing/', views.ongoing_projects, name="ongoing"),
  path('createproject/', views.CreateProjectView.as_view(), name="createproject"),
  path("<int:pk>/room/create/", views.create_room, name="createroom"),
  path('<int:project_id>/room/<int:room_id>/update/', views.update_room, name="updateroom"),
  path('<int:project_id>/room/<int:room_id>/delete/', views.DeleteRoomView.as_view(), name="deleteroom"),
  path('<int:project_id>/complete/', views.complete_project, name="complete_project"),
  path('<int:pk>/', views.ProjectDetailView.as_view(), name='projectdetail'),
  path('<int:pk>/update/', views.ProjectUpdateView.as_view(), name='update'),
]
