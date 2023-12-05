from django.contrib import admin
from django.urls import path, include
from .views import helloworldFunction, helloJsonResponse
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # hello world app
    path('helloworldapp/', include('helloworldapp.urls')),
    
    # todo list app
    path('todo/', include('todoapp.urls')),
    
    # sns app
    path("sns/", include('snsapp.urls')),
    
    # function based view サンプル
    path('helloResponse', helloworldFunction),
    path('jsonResponse', helloJsonResponse)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
