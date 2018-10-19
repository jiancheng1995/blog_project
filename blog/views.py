from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BolgDetailView(DetailView):
    model= Post
    template_name= 'Post_detail.html'
    content_object_name='anything_you_want'