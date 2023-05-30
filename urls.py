from django.contrib import admin
from django.urls import path,include
from WebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('create/',views.org_create),
    path('retrive/<int:id>',views.org_retrive,name='retrive'),
    path('update/<int:id>',views.org_update,name='update'),
    path('delete/<int:id>',views.org_delete,name='delete'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)