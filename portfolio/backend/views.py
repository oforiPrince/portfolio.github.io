from xml.sax.saxutils import prepare_input_source
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from blog.models import Blog
from blog.forms import BlogForm


class DashboardView(View):
    def get(self, request):
        template_name = 'pages/index.html'

        return render(request, template_name)


class ProfileView(View):
    def get(self, request):
        template_name = 'pages/profile.html'

        return render(request, template_name)


class BlogsView(View):
    def get(self, request):
        template_name = 'pages/blogs.html'
        blogs = Blog.objects.all().order_by('-date_created')
        context = {
           'blogs': blogs
        }
        return render(request, template_name,context)


class CreateBlogView(View):
    def get(self, request):
        template_name = 'pages/create_blog.html'
        form = BlogForm()
        context = {
            'form': form
        }
        return render(request, template_name,context)

    def post(self,request):
        template_name = 'pages/blogs.html'
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            owner = form.cleaned_data['owner']
            body = form.cleaned_data['body']
            tags = form.cleaned_data['tags']
            print(title,tags)
            return render(request, template_name)
        else:
            print(form.errors)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
