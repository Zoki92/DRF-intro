
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    # path('api-auth/',
    #      include('rest_framework.urls',
    #              namespace='rest_framework')),
    # path('puppies/', include('puppies.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('', include('catalog.urls')),


]
