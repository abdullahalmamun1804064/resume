
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeview.as_view(),name='home'),
    path('<int:id>', views.Candate.as_view(),name='candate'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
