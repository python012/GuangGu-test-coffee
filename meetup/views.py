from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request, 'index.html', {'error_message': 'username or password is not correct!'})


@login_required
def event_manage(request):
    username = request.session.get('user', '')
    return render(request, 'event_manage.html', {'user':username})