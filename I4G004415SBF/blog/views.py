
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
# Create your views here.
class PostCreateView(CreateView):
    model: Post
    fields= "__all__"
    success_url = reverse_lazy("blog:all")

class PostListView(ListView):
    model = Post
    

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model= Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model= Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")