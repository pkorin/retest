from django.conf.urls import include, url, patterns
from django.contrib import admin
from mysite.views import hello,current_datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    ('^hello/$',hello),
    ('^current/$',current_datetime),

)
