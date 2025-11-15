"""
URL configuration for modal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("product/create/", views.product_create, name="product_create"),
    path("product/update/<int:pk>/", views.product_update, name="product_update"),
    path("product/delete/<int:pk>/", views.product_delete, name="product_delete"),
    re_path(r"^.*/$", views.page_not_found),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
