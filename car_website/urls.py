from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('account_app.urls')),
    path('brand/<slug:brand_slug>', views.home, name='brand_wise_filter'),
    path('view_details/<int:id>', views.view_details, name='view_details'),
    path('view_details/buy_car/<int:id>', views.buy_car, name='buy_car'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)