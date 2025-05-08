from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
from django.http import JsonResponse
# Create your views here.
def index(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return JsonResponse({"msg": "successs"})
    
  form = ContactForm()
  return render(request, 'app/index.html', {'form': form})


