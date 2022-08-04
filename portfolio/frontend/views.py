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
        blogs = Blog.objects.all().order_by('-publish_date')
        categories = Category.objects.all()
        frameworks = FriendlyFrameWork.objects.all()
        services = Service.objects.all()
        schools = School.objects.all()
        testimonials = Testimonial.objects.all()
        projects = Project.objects.all()
        project_types = ProjectType.objects.all()
        context = {
            'user': user,
            'resumes': resumes,
            'certificates': certificates,
            'knowledges': knowledges,
            'blogs': blogs,
            'categories': categories,
            'frameworks':frameworks,
            'services':services,
            'schools':schools,
            'testimonials':testimonials,
            'projects':projects,
            'project_types':project_types,
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


class AboutView(View):
    def get(self, request):
        template_name = 'website/pages/about.html'
        user = User.objects.all().first()
        frameworks = FriendlyFrameWork.objects.all()
        schools = School.objects.all()
        projects = Project.objects.all()
        context = {
            'user': user,
            'frameworks':frameworks,
            'schools':schools,
            'projects':projects,
        }
        return render(request, template_name, context)
    
class ServicesView(View):
    def get(self, request):
        template_name = 'website/pages/services.html'
        user = User.objects.all().first()
        context = {
            'user': user
        }
        return render(request, template_name, context)

class ResumeView(View):
    def get(self,request):
        template_name = 'website/pages/resume.html'
        
        return render(request, template_name)

class ProjectsView(View):
    def get(self, request):
        template_name = 'website/pages/projects.html'
        user = User.objects.all().first()
        projects = Project.objects.all()
        context = {
            'user': user,
            'projects': projects
        }
        return render(request, template_name, context)
    
class BlogView(View):
    def get(self, request):
        template_name = 'website/pages/blog.html'
        user = User.objects.all().first()
        blogs = Blog.objects.all().order_by('-publish_date')
        tags = Tag.objects.all()
        context = {
            'user': user,
            'blogs': blogs,
            'tags': tags
        }
        return render(request, template_name, context)

class ContactView(View):
    def get(self, request):
        template_name = 'website/pages/contact.html'
        user = User.objects.all().first()
        context = {
            'user': user
        }
        return render(request, template_name, context)

class BlogDetailView(View):
    def get(self, request, id):
        template_name = 'website/pages/blog-detail.html'
        blog = Blog.objects.get(pk=id)
        latest_blogs = Blog.objects.all().order_by('-id')[:4]
        # print(latest_blogs)
        context = {
            'blog': blog,
            'latest_blogs': latest_blogs
        }
        return render(request, template_name, context)

