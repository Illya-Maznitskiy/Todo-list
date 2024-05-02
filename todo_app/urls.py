from django.urls import path, include

from todo_app import views

urlpatterns = [
    path('', include("todo_app.urls"), namespace="todo_app"),
]
