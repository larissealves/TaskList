from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="list"),
    path('updateTask/<str:pk>/', views.updateTask, name="update_task"),
    path('deleteTask/<str:pk>/', views.deleteTask, name="delete"),
    path('description/',views.createDescriptions, name="create_description"),
    path('details/<str:pk>/', views.details, name="details"),
]+ static(settings.STATIC_URL)