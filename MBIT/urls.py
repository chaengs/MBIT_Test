from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), #include를 import 해야함
    # main폴더의 urls.py로 연결됨
    # path('a', include('main.urls')) 이면 기본url/a/main폴더의urls.py로 연결  
]