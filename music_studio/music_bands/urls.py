from django.urls import path
from.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('bands/', BandListView.as_view(), name='band-list'),
    path('bands/<int:pk>/', BandDetailView.as_view(), name='band-detail'),
    path('bands/add/', BandCreateView.as_view(), name='band-add'),
    path('bands/<int:pk>/edit/', BandUpdateView.as_view(), name='band-edit'),
    path('bands/<int:pk>/delete/', BandDeleteView.as_view(), name='band-delete'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]