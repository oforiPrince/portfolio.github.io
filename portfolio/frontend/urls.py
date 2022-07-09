from django.urls import path
from . import views
app_name = 'frontend'
urlpatterns = [
    path('',views.indexView.as_view(),name='index'),
    path('blog/<int:pk>/detail',views.BlogDetailView.as_view(),name='blog_detail'),
]
