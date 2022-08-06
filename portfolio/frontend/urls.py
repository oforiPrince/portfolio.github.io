from django.urls import path
from . import views
app_name = 'frontend'
urlpatterns = [
    path('',views.indexView.as_view(),name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('services/',views.ServicesView.as_view(),name='services'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('resume/',views.ResumeView.as_view(),name='resume'),
    path('projects/',views.ProjectsView.as_view(),name='projects'),
    path('blog/',views.BlogView.as_view(),name='blogs'),
    path('send_mail',views.SendMailView.as_view(),name='send_mail'),
    
    path('blog/detail/<int:id>/',views.BlogDetailView.as_view(),name='blog_detail'),
]
