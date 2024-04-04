from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from users.views import confirm_email

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('mail.urls'), name='mail'),
    path('users/', include("users.urls"), name='users'),
    path('users/activate/<str:token>/', confirm_email, name='email_verification'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
