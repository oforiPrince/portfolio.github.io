from django.shortcuts import render
from django.views import View
from blog.models import Blog


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

        return render(request, template_name)
