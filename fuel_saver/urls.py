"""
URL configuration for fuel_saver project.

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
#you have to use an "import" to get info from other files  "from . import views"  gives us access to the views.py file within this same directory, for example


from django.contrib import admin
from django.urls import path 
from . import views
from .views import calculate_fuel

#paths are the url routes to the info referred to.  So "path('about/', views.about)"  tells us what to apply when /about is added to the url.
#It gets the info from the views.py by calling the file then the method defined within the file (views.about, for example).

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/', views.homepage),
    #path('about/', views.about),
    #path('', views.index),
    path("", calculate_fuel, name="calculate_fuel")

]
