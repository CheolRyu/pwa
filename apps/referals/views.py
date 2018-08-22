from django.shortcuts import render, redirect
from apps.home.models import User
# Create your views here.
def index(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/login')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'referals/index.html', context)
