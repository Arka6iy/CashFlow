"""
URL configuration for TestTask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from app.views import (HomeView, delete_transaction, edit_transaction, form,
                       get_categories, get_subcategories)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("edite/", form, name="form"),
    path("get_categories/", get_categories, name="get_categories"),
    path("get_subcategories/", get_subcategories, name="get_subcategories"),
    path("edit/<int:pk>/", edit_transaction, name="edit_transaction"),
    path("delete/<int:pk>/", delete_transaction, name="delete_transaction"),
]
