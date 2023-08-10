from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('charityapp.common.urls')),
    path('causes/', include('charityapp.causes.urls')),
    path('blog/', include('charityapp.blog.urls')),
    path('contact/', include('charityapp.contact.urls')),
    path('profile/', include('charityapp.user_profiles.urls')),
    # path('user_accounts/', include('allauth.urls')),
    path('accounts/', include('charityapp.user_accounts.urls')),
    path('about/', include('charityapp.about.urls')),
    path('get-involved/', include('charityapp.get_involved.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
