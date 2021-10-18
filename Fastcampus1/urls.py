from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('order/', include('order.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('boss/', include('boss.urls')),
    path('delivery/', include('delivery.urls'))
]


