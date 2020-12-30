from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book, Comment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

#def home(request):
 #   context = {
  #      'posts' : Book.objects.all(),
   #     'title' : 'Home'
    #}

    #return render(request, 'blog/home.html',context)

class BookListView(ListView):
    model = Book
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class BookDetailView(DetailView):
    model = Book

class AddCommentView(CreateView):
    model = Comment
    #template_name = 'add_comment.html'
    fields = ('content',)
    ordering = ['-date_commented']

    def form_valid(self, form):
        form.instance.commented_post_id = self.kwargs['pk']
        form.instance.username = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('blog-home')

def about(request):
    return render(request, 'blog/about.html', { 'title' : 'About' })

def fiction(request):
    context = {
        'posts' : Book.objects.all().filter(genre='Fiction'),
        'title' : 'Home'
    }
    return render(request, 'blog/fiction.html', context)
