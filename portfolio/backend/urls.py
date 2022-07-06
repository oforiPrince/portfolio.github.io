from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
    path('',views.DashboardView.as_view(),name='dashboard'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('blogs/',views.BlogsView.as_view(),name='blogs'),
    path('create_blog/',views.CreateBlogView.as_view(),name='create_blog'),
]
