from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Accounts
    url(r'^', include('apps.accounts.urls')),
    # Social
    url(r'^oauth/', include('social_django.urls')),
    # VK
    url(r'^', include('apps.vk.urls')),
]



# For serve static, media, templates in develop mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/templates/', document_root=settings.BASE_DIR + '/templates/')
