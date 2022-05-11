from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blogs, Likes, Comments
from .forms import BlogForm, LikeForm,CommentForm
from django.urls import reverse






class BlogListView(LoginRequiredMixin, ListView):

    def get(self,request):
        Blog = Blogs.objects.all().order_by('-id')
        context = {'blog_list': Blog}
        
        return render(request, "Blog/blogs_list.html", context)

class BlogDetailView(LoginRequiredMixin, DetailView):
    template_name = 'Blog/blog_detail.html'
    model = Blogs
    

    def get_context_data(self,*args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        pk = self.kwargs['pk']
        Like = Likes.objects.filter(post_id = pk).count()
        comment = Comments.objects.filter(post_id = pk).order_by('-id')[:3]
        context['likes'] = Like
        context['comment'] = comment
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
    template_name = 'Blog/blog_update.html'
    form_class = BlogForm
    login_url = '/login/'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Blogs.objects.filter(id=pk)




class LikesCreateView(LoginRequiredMixin, CreateView):
    template_name = "Blog/blog_detail.html"
    form_class = LikeForm
    login_url = '/login/'

    def form_valid(self, form):               
        obj = form.save(commit=False)
        obj.status = True
        return super(LikesCreateView, self).form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = "Blog/blog_detail.html"
    form_class = CommentForm
    login_url = '/login/'

    def form_valid(self, form):               
        obj = form.save(commit=False)
        return super(CommentCreateView, self).form_valid(form)