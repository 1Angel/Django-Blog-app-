from django.urls import path, include
from post.views import IndexView, DetailsView, AboutView, CreatePostView, RegisterView, LoginView, logoutView, ProfileView
urlpatterns = [
    path('', IndexView, name='index'),
    path('post/<int:pk>', DetailsView, name='details'),
    path('about', AboutView, name='about'),
    path('post/create', CreatePostView, name='create-post'),
    path('auth/register', RegisterView, name="register"),
    path('auth/login', LoginView, name='login'),
    path('auth/logout', logoutView, name='logout'),
    path('auth/profile', ProfileView, name='profile')
]