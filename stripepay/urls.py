from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from stripepay import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('item/', include('item.urls')),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
