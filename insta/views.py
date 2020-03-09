from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from insta.models import Post
# Create your views here.
class Helloworld(TemplateView):
        template_name = 'test.html'

class PostView(ListView):
    model = Post
    template_name = 'index.html'
