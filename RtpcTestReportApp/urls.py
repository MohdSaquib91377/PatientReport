
from django.urls import path
from .views import dashboard,view_report,download_report
urlpatterns = [
    path('', dashboard,name='dashboard'),
    path('view_report/', view_report,name='view_report'),
    path('download_report/',download_report,name='download_report')
]
