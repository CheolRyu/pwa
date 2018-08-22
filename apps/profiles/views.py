from django.shortcuts import render, redirect
from apps.home.models import User

# Create your views here.

def index(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user':user,
    }
    return render(request, 'profiles/index.html', context)


def edit(request, user_id):
    user = User.objects.get(id=id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.save()
    return redirect('/')
