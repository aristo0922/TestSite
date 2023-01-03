from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>', posting, name="posting"),
    path("blog/<int:pk>/remove/", remove_post),
]
