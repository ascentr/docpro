"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from core import views as V

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(), name="index"),
#    path('core/', include('core.urls', namespace='core')),
#    path("core/sign/", V.sign, name="sign"),
    path("core/roomlist/", V.room_list, name="roomlist"),
    path("core/createroom/", V.create_room, name="createroom"),
#    path('core/createproject/',V.ProjectCreateView.as_view(), name='createproject'),
    path('core/createproject/', V.ProjectCreateView, name='createproject'),
    path('core/projectlist/',V.ProjectListView.as_view(), name='projectlist'),
    path('core/selectproject/', V.get_project, name='selectproject'),
    path('core/projectlist/<int:pk>/',V.ProjectDetailView.as_view(), name='projectdetail'),
    path('core/update/<int:pk>/',V.ProjectUpdateView.as_view(), name='update'),
    path('core/delete/<int:pk>/',V.ProjectDeleteView.as_view(), name='delete'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 