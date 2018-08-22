from django.shortcuts import render, redirect
from apps.home.models import User

def index(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    return render(request, 'articles/index.html')
