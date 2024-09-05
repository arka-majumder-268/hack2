from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drug_track.urls')),
]



urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('vendor/<int:vendor_id>/', views.vendor_activity, name='vendor_activity'),
    path('hospital/<int:hospital_id>/', views.hospital_activity, name='hospital_activity'),
]