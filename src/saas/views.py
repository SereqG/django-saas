from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_title = "My page"

    context = {"page_title": page_title, "queryset": queryset}

    template = "home.html"
    PageVisit.objects.create()
    return render(request, template_name=template)
