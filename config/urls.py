from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from urllib.parse import urlparse
from django.http import HttpResponseRedirect


def set_language(request, language):
    translation.activate(language)

    referer = request.META.get("HTTP_REFERER")
    if referer:
        try:
            view = resolve(urlparse(referer).path)
            next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        except Resolver404:
            next_url = "/"
    else:
        next_url = "/"

    response = HttpResponseRedirect(next_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path("set_language/<str:language>", set_language, name="set-language"),
    prefix_default_language=True
)