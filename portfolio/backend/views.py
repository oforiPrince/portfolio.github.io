from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from blog.models import Blog, Tag, Category
from blog.forms import BlogForm, CategoryForm, TagForm


class DashboardView(View):
    def get(self, request):
        template_name = 'pages/index.html'
        
        context = {
            'page_title': 'Dashboard',
        }
        return render(request, template_name,context)


class ProfileView(View):
    def get(self, request):
        template_name = 'pages/profile.html'
        context = {
            'page_title': 'Profile',
        }
        return render(request, template_name,context)


class BlogsView(View):
    def get(self, request):
        template_name = 'pages/blogs.html'
        blogs = Blog.objects.all().order_by('-date_created')
        context = {
            'blogs': blogs,
            'page_title': 'Blogs',
        }
        return render(request, template_name, context)


class CreateBlogView(View):
    def get(self, request):
        template_name = 'pages/create_blog.html'
        form = BlogForm()
        context = {
            'form': form,
            'page_title': 'Create Update Blog',
        }
        return render(request, template_name, context)

    def post(self, request):
        template_name = 'pages/blogs.html'
        form = BlogForm(request.POST, request.FILES)
        blogs = Blog.objects.all().order_by('-date_created')
        context = {
            'blogs': blogs,
            'page_title': 'Blogs',
        }
        if form.is_valid():
            form.save()
            messages.success(request, "Blog created successfully")
            return render(request, template_name, context)
        else:
            print(form.errors)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CategoriesView(View):
    def get(self, request):
        template_name = 'pages/categories.html'
        categories = Category.objects.all()
        print(categories)
        context = {
            'page_title': 'Categories',
        }
        return render(request, template_name,context)


class CreateUpdateCategoryView(View):
    def get(self, request):
        template_name = 'pages/create_update_category.html'
        form = CategoryForm()
        context = {
            'form': form,
            'page_title': 'Create Update Category',
        }
        return render(request, template_name,context)

    def post(self, request):
        template_name = 'pages/categories.html'
        form = CategoryForm(request.POST)
        categories = Category.objects.all()
        print(categories)
        context = {
            'categories': categories,
            'page_title': 'Categories',
        }
        if form.is_valid():
            for category in categories:
                if category.name == form.cleaned_data['name']:
                    messages.error(request, "Category already exists")
                    return render(request, template_name, context)
                form.save()
                messages.success(request, "Category created successfully")
                return render(request, template_name, context)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class TagsView(View):
    def get(self, request):
        template_name = 'pages/tags.html'
        tags = Tag.objects.all()
        print(tags)
        context = {
                'page_title': 'Tags',
            }
        return render(request, template_name,context)


class CreateUpdateTagView(View):
    def get(self, request):
        template_name = 'pages/create_update_tag.html'
        form = TagForm()
        context = {
            'form': form,
            'page_title': 'Create Update Tag'
        }
        return render(request, template_name,context)

    def post(self, request):
        template_name = 'pages/tags.html'
        form = TagForm(request.POST)
        tags = Tag.objects.all()
        context = {
            'tags': tags,
            'page_title': 'Tags',
        }
        if form.is_valid():
            name = form.cleaned_data.get('name')
            for name in tags:
                if name == name:
                    messages.error(request, "Tag already exists")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                form.save()
                messages.success(request, "Tag created successfully")
                return render(request, template_name, context)
        else:
            print(form.errors)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
