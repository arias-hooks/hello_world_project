from django.contrib import admin
from django.urls import include, path

from .views import HelloWorldClass, hello_world_function, some_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', hello_world_function),
    path('helloworld2/', HelloWorldClass.as_view()),
    path('someview/', some_view),
    path('app/', include('helloworldapp.urls')),
]
