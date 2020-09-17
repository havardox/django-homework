from django.urls import path
from .views import (
    api_overview,
    homework_list,
    homework_detail,
    homework_create,
    homework_update,
    homework_delete,
)

urlpatterns = [
    path('', api_overview, name="api-overview"),
    path('homework-list/', homework_list, name="homework-list"),
    path('homework-detail/<str:pk>/', homework_detail, name="homework-detail"),
    path('homework-create/', homework_create, name="homework-create"),
    path('homework-update/<str:pk>/', homework_update, name="homework-update"),
    path('homework-delete/<str:pk>/', homework_delete, name="homework-delete"),
]
