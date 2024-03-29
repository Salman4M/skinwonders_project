"""core URL Configuration

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
from django.urls import path,include
from django.utils.translation import gettext_lazy as _ 

from django.conf.urls.i18n import i18n_patterns

from products.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.api.urls")),
    path('products/', include("products.api.urls")),
    path('content/', include("content.api.urls")),


]


urlpatterns += [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>/",views.LanguageSwitchAPIView.as_view(), name="set-language"),

    ]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
