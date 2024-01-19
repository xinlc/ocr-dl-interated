from django.urls import path

from . import views

urlpatterns = [
  path('upload-image', views.paddle_image_upload),
  path('login', views.logins),
  path('orc-records', views.one_ocr_record),
  path('register', views.register),
  path('delete/record', views.delete_record)

]
