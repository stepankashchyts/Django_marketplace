from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'item'
urlpatterns = [
    path("new/", views.new, name="new"),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('browse/', views.browse, name='browse')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
