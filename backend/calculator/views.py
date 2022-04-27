from django.shortcuts import render
from .forms import CalculatorForm


def index(request):
    calcform = CalculatorForm()
    return render(request, "index.html", {"form": calcform})