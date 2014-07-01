from django.conf.urls import url, patterns


urlpatterns = patterns(
    '',
    url(r'^all/$', 'art_blog.views.main_page', name='main'),
    url(r'^get/(?P<article_id>\d+)/$',
        'art_blog.views.content', name='content'),
    url(r'^add_article/$', 'art_blog.views.add_article', name='add_article'),
    url(r'^edit_article/(?P<article_id>\d+)',
        'art_blog.views.edit_article', name='edit_article'),
    url(r'^add_comment/(?P<article_id>\d+)/$',
        'art_blog.views.add_comment', name='blog'),
)
