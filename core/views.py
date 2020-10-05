from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
import json

# Create your views here.

@login_required(login_url='/login')
def index(request):
  obj = {}
  obj = apiAccess()
  print(obj)
  return render(request, 'index.html', obj)

def logout_user(request):
  logout(request)
  return redirect('/login/')  

def login_user(request):
  return render(request, 'login.html')

@csrf_protect
def submit_login(request):
  if request.POST:
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      messages.error(request, 'Usuário e/ou senha inválido(s). Tente novamente.')
  return redirect('/login/')

def apiAccess():
  url = 'http://www.omdbapi.com/?t=Avengers&apikey=6d03e916'
  response = requests.get(url)
  r_json = json.loads(response.content)
  if 'Error' not in r_json:
    print(r_json)
    print(r_json['Title'])
    print(r_json['Poster'])
    obj = r_json
    obj = {'movieList': obj}
    return obj
          