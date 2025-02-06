"""
URL configuration for companyapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from .views import home_page

# URL patterns for the project
urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),
    
    # A custom home page URL, mapped to the 'home_page' view
    path("home/", home_page),
    
    
    # Include API URLs without /api/v1/ prefix
    path('', include('api.urls')),  # This makes 'ui/' accessible directly at root
    # Include URLs for the API version 1. This will route requests starting with /api/v1/ to the api.urls module
    # path("api/v1/", include('api.urls'))
]
