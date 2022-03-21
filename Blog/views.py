from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blogs
from .forms import BlogForm
from django.urls import reverse






class BlogListView(LoginRequiredMixin, ListView):
    model = Blogs
    template_name = 'Blog/ListView'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        Blog = Blogs.objects.all()
        
        context['blog_list'] = Blog  
        return context

	

class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = "Blog/blog_create.html"
    form_class = BlogForm
    login_url = '/login/'

    def form_valid(self, form):               
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(BlogCreateView, self).form_valid(form)




class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'Users/update_profile.html'
    form_class = BlogForm
    login_url = '/login/'

    def get_queryset(self):
        return Blogs.objects.filter(user=self.request.user)




class LikesCreateView(LoginRequiredMixin, CreateView):
    template_name = "Blog/blog_create.html"
    form_class = BlogForm
    login_url = '/login/'

    def form_valid(self, form):               
        obj = form.save(commit=False)
        # obj.post   = self.request.user
        # obj.status = self.request.user
        return super(LikesCreateView, self).form_valid(form)