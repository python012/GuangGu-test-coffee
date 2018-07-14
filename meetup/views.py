from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from meetup.models import MeetupEvent, Topic


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
            return HttpResponseRedirect('/topics_list/')
        else:
            return render(request, 'index.html', {'error_message': 'username or password is not correct!'})


@login_required
def topics_list(request):
    username = request.session.get('user', '')
    topics_list = Topic.objects.all()
    
    return render(request, "topics_list.html", {"user": username, "topics": topics_list})
