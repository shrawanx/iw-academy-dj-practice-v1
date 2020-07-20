from django.urls import path, register_converter, include

from world.views import (home, profile, profile_json,
                         int_converter_view, debug_request,
                         test_args_kwargs)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


# regex, to_python(), to_url()
class YearPathConverter:
    regex = '[0-9]{4}'

    @staticmethod
    def to_python(value):  # yo method-->ValueError
        int_data = int(value)

        if int_data > 2020:
            raise ValueError

        return int_data

    @staticmethod
    def to_url(value):
        return str(value)


register_converter(YearPathConverter, 'yyyy')

urlpatterns = [
    path('profile/<str:username>/', profile),
    path('profile-json/<str:username>/', profile_json),
    path('path/<str:int_data>/', int_converter_view),
    path('test-path/', debug_request),
    path('', home),
    path('example/<yyyy:int_data>/', int_converter_view),
    path('test/<int:data>/', test_args_kwargs),
    path('template/', include('templating.urls')),
    path('forms/', include('formspractice.urls')),
    path('static-demo/', include('staticmedia.urls')),

    path('crud/', include('crud.urls', namespace='crud')),
    path('c/', include('classbased.urls', namespace='classbased')),

    path('statusapp/', include('statusapp.urls', namespace='statusapp')),

    path('accounts/', include('accounts.urls')),
    path('rest/', include('rest.urls')),

    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    # debug=false
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
