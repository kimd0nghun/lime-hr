"""limehr URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from evaluation.utils import set_cache_data
from django.conf import settings
from config.views import *
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('', home_view, name='main'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('eval/', include('evaluation.urls')),
    path('journal/', include('journal.urls')),
    path('mdm/', include('mdm.urls')),
    path('manage/', include('management.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('api-auth/', include('rest_framework.urls'))
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = server_error

# 캐쉬 데이터 로딩
set_cache_data()
