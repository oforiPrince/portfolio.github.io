from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('create_blog/', views.CreateBlogView.as_view(), name='create_blog'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('create_update_category/', views.CreateUpdateCategoryView.as_view(),
         name='create_update_category'),
    path('tags/', views.TagsView.as_view(), name='tags'),
    path('create_update_tag/', views.CreateUpdateTagView.as_view(),
         name='create_update_tag'),
    path('blog_detail/',
         views.BlogDetailView.as_view(), name='blog_detail'),
    path('update_blog/',
         views.UpdateBlogView.as_view(), name='update_blog'),
    path('delete_blog/',
         views.DeleteBlogView.as_view(), name='delete_blog'),
]
