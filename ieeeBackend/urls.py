from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'IEEE LINK Web Login Panel'                    # default: "Django Administration"
admin.site.index_title = 'Admin Arena'                 # default: "Site administration"
admin.site.site_title = 'IEEE Kerala Section - LINK Team' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('',include('posts.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)