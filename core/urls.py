from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
	path('dash/', include('dash.urls')),
    path('web/', include('web.urls')),
]
