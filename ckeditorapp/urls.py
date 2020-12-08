from django.urls import path, include
from . import views

app_name = 'ckeditorapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail<int:post_id>', views.detail, name='detail'),
    path('add_form', views.add_form, name='add_form'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
