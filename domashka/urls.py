from django.urls import path

from . import views


urlpatterns = [
    path("", views.StudentDetailView.as_view(), name="student_detail"),
]