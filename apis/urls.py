from django.urls import path

from . import views

urlpatterns=[
    path('', views.getRoutes),
    path('health/score/', views.getHealthScore),
    path('train/<str:choice>/', views.training),
    path('data/', views.getData),
    path('limits/', views.getLimits),
    path('create/data/', views.postData),
    path('upload/', views.upload_file),
    path('exportValues/', views.exportCSV),
    path('exportData/', views.exportExcel)
]