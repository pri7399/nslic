from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', include('home.urls')),
    path('', RedirectView.as_view(url="home/")),
    path('Plan/', include('home.urls')),

    path('admin/', admin.site.urls),

]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
