from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from backend.models import *
from accounts.models import User
from blog.models import Blog, Tag, Category


class indexView(View):
    def get(self, request):
        template_name = 'website/pages/index.html'
        user = User.objects.all().first()
        resumes = Resume.objects.all()
        certificates = Certificate.objects.all()
        knowledges = Knowledge.objects.all()
      #   blogs = Blog.objects.all().order_by('-publish_date')
        categories = Category.objects.all()
        context = {
            'user': user,
            'resumes': resumes,
            'certificates': certificates,
            'knowledges': knowledges,
            # 'blogs': blogs,
            'categories': categories
        }
        return render(request, template_name, context)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(name, email, subject, message)
        messages.success(request, "email sent successfully")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class BlogDetailView(View):
    def get(self, request, pk):
        template_name = 'website/blog_detail.html'
        blog = Blog.objects.get(pk=pk)
        context = {
            'blog': blog
        }
        return render(request, template_name, context)

