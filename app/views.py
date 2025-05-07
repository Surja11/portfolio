from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
from django.http import JsonResponse
# Create your views here.
def index(request):
  form = ContactForm()
  return render(request, 'app/index.html', {'form': form})


