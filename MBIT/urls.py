from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('form/', views.form),
    path('submit/', views.submit),
    path('result/<int:developer_id>', views.result),
]
