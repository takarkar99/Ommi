from django.contrib import admin
from django.urls import path
from App1.views  import ScheduleAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', ScheduleAPI.as_view(), name='Scheduler')
]
