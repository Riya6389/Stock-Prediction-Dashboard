
from django.contrib import admin
from django.urls import path, include   # ✅ include bhi import karna hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stock.urls')),   # ✅ Yahan stock.urls ko include karna hoga
]
