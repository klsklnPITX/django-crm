from django.shortcuts import render
from django.http import HttpResponse

from .models import Lead


def home_page(request):
    # return render(request, "leads/home_page.html")

    leads = Lead.objects.all()
    context = {
        "leads": leads
    }

    return render(request, "second_page.html", context)
