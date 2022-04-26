from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView

# Create your views here.
class BlogListView(ListView):
    model=Blog
    template_name='home.html'

class BlogCreateView(LoginRequiredMixin,CreateView):
    model=Blog
    template_name='post_new.html'
    fields=('title','body')
    
    def form_valid(self, form): 
        return super().form_valid(form)



class BlogDetailView(LoginRequiredMixin,DetailView):
    model=Blog
    template_name='post_detail.html'

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model=Blog
    template_name='post_update.html'
    fields=['title','body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
        