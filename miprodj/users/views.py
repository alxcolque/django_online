from django.shortcuts import render
from .models import User

# Create your views here.
def inicio(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users/inicio.html', context)