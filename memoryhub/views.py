from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import memoryhub
from .models import Memory

# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  memories = reversed(Memory.objects.all())
  return render(request, 'home.html', {'memories': memories})

@login_required
def create(request):
  # Memory.objects.create(location = 'meme', comment = 'mememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememememe', created_at = '07-Oct-21')
  # memories = Memory.objects.all().delete()
  if request.method == 'POST':
    location, comment = request.POST.get('location'), request.POST.get('comment')
    if location and comment:
      memory = Memory(location = location, comment = comment)
      memory.save()
      return redirect('home')
    
    else:
      return render(request, 'memorycreation.html')

  else:
    return render(request, 'memorycreation.html')

