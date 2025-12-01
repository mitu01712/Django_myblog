from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public Views
    path('', views.PostListView.as_view(), name='home'),
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='post_by_tag'),
    
    # Dashboard & CRUD Operations 
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  
    
    # Post Detail & Specific Actions
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/like/', views.like_post, name='like_post'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'), 

    # Authentication (Register Path Added Here)
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]