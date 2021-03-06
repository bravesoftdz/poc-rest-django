"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

from quickstart.api import PostResource

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^api/v2/', include(router.urls)),
    url(r'^api/v2/docs', schema_view),

    url(r'api/v1/posts/', include(PostResource.urls())),
]

