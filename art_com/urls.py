from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('art_blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'art_com.views.login', name='login'),
    url(r'^auth_user/$', 'art_com.views.auth_user', name='auth_user'),
    url(r'^loggedin/$', 'art_com.views.loggedin', name='loggedin'),
    url(r'^logout/$', 'art_com.views.logout', name='logout'),
    url(r'^invalid/$', 'art_com.views.invalid', name='invalid'),
    url(r'^register_user/$', 'art_com.views.register_user',
        name='register_user'),
    url(r'^register_success/$', 'art_com.views.register_success',
        name='register_success'),
)
