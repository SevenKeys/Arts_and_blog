from django.conf.urls import url, patterns


urlpatterns = patterns(
    '',
    url(r'^$', 'art_blog.views.main_page', name='main'),
    url(r'^get/(?P<article_id>\d+)/$',
        'art_blog.views.content', name='content'),
    url(r'^add_article/$', 'art_blog.views.add_article', name='add_article'),
    url(r'^edit_article/(?P<article_id>\d+)',
        'art_blog.views.edit_article', name='edit_article'),
    url(r'delete_article/(?P<article_id>\d+)/$',
        'art_blog.views.delete_article',name='delete_article'),
    url(r'^add_comment/(?P<article_id>\d+)/$',
        'art_blog.views.add_comment', name='blog'),
    url(r'delete_comment/(?P<comment_id>\d+)/$',
        'art_blog.views.delete_comment',name='delete_comment'),
    url(r'^articles/search/$','art_blog.views.search_results',name='search_results'),
)
