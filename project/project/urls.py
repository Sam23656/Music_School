"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from music_school.views import show_index_page, show_student_page, show_register_page, show_student_edit_page

urlpatterns = [
    path('', show_index_page),
    path('admin/', admin.site.urls),
    path('register/', show_register_page),
    path('<int:student_id>/', show_student_page),
    path('edit/<int:student_id>/', show_student_edit_page)
]
