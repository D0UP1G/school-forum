from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib.auth import login
from django.shortcuts import redirect
from user.models import User
import random
from .forms import *

class MainView(View):
    def get(self,requests):
        threads = PostModel.objects.filter(hidden = False)
        tags = TagsModel.objects.all()
        return render(requests, 'main/index.html', {'posts':threads, 'tags':tags})

class ThreadCreate(View):
    def get(self, requests):
        form = PostForm()
        return render(requests, 'threads/index.html', {'form':form,})
    def post(self, requests):
        form = PostForm(requests.POST)
        if form.is_valid():
            # Обработка данных формы
            post = form.save(commit=False)  #
            post.owner = requests.user
            post.save()
            return redirect('home')
        return render(requests, 'threads/index.html', {'form':form,})

def auto_login(reqeusts):  
    user = User.objects.filter(is_superuser=True)
    login(reqeusts, user[random.randint(1, len(user))-1])
    return redirect('home')


class TagView(View):
    def get(self,requests, tag):
        threads = PostModel.objects.filter(tags__url=tag, hidden=False)
        tags = TagsModel.objects.all()
        return render(requests, 'main/index.html', {'posts':threads, 'tags':tags})
