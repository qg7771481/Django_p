from django.shortcuts import render
from django.views.generic import DetailView

from .models import Student


class StudentDetailView(DetailView):
    """Детальна інформація про пост."""

    queryset = Student.objects.select_related("group", "library_card")
    context_object_name = "student"
    template_name = "domashka/student_detail.html"
