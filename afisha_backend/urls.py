"""afisha_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cinema/',views.print_cinema),
    path('api/v1/cinema/<int:id>/',views.print_cinema_id),
    path('api/v1/movies/',views.print_movie),
    path('api/v1/movies/<int:id>/',views.print_movie_id),
    path('api/v1/movies/reviews/',views.print_review),
    path('api/v1/movies/genres/',views.print_genres),
    path('api/v1/movies/delete-update/<int:id>',views.delete_put_movie),
    path('api/v1/movies/create_view_movie/',views.create_view_movie),
    path('api/v1/movies/login/',views.login),
    path('api/v1/movies/registration/',views.registration),

]
