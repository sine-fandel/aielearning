from django.urls import path
from . import views

urlpatterns = {
    path("helloApi", views.hello, name='hello'),
    path ("uploadApi", views.uploadapi, name="uploadapi"),
    path ("gen_examapi", views.gen_examapi, name="gen_examapi"),
    path ("search_examapi", views.search_examapi, name="seach_examapi"),
    path ("register", views.register, name="register"),
    path ("login", views.login, name="login"),
}