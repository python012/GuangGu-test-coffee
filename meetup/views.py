from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def index(request):
    return render(request, "index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == "admin" and password == "admin123":
            return render(request, 'index.html', {'error_message': '!!greate user!!'})

        # user = auth.authenticate(username=username, password=password)

        # if user is not None:
        #     auth.login(request, user)
        #     request.session['user'] = username
        #     response = HttpResponseRedirect('/event_manage/')
        #     return response
        # else:
        #     return render(request, 'index.html', {'error_message': 'username or password is not correct!'})