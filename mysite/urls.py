"""
URL configuration for mysite project.

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

import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(os.environ.get('ADMIN_PATH'), admin.site.urls),
    path("", login_required(TemplateView.as_view(template_name="root.html")), name="root"),
    path(route="introduction/", view=include("introduction.urls")),
    path(route="accounts/", view=include("accounts.urls")),
    path(route="", view=include("portfolio.urls")),
    path(route="", view=include("blog.urls")),
    # path(route="ckeditor/", view=include('ckeditor_uploader.urls')),
    # path('tinymce/',include('tinymce.urls')), # new
    
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
