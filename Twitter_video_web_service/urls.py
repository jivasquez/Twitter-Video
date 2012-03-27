from django.conf.urls.defaults import patterns, include, url
from twitter_video.controllers import upload
from django.conf import settings
from twitter_video import VIDEO_DIR

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Twitter_video_web_service.views.home', name='home'),
    # url(r'^Twitter_video_web_service/', include('Twitter_video_web_service.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^upload/form', 'twitter_video.controllers.upload.upload_form'),# for debugging purposes only
    (r'^upload/upload_video', 'twitter_video.controllers.upload.upload_video'),
    (r'^list', 'twitter_video.controllers.list.list_videos'),
    (r'^api/list', 'twitter_video.controllers.list.api_list_videos'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': VIDEO_DIR}),
)
