from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')

class BookmarkListView(ListView):
    model = Bookmark

#(creatview)를 상속받는다.
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_create'
    success_url = reverse_lazy('list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'
    
    # 안적어주면 bookmark_form 으로 가져옴. create update 분리위해 설정

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    template_name_suffix = '_delete'
    