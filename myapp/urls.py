from django.contrib import admin
from django.urls import path, include
from .views import helloworldFunction, helloJsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # hello world app
    path('helloworldapp/', include('helloworldapp.urls')),
    
    # todo list app
    path('todo/', include('todoapp.urls')),
    
    # function based view サンプル
    path('helloResponse', helloworldFunction),
    path('jsonResponse', helloJsonResponse),
]
