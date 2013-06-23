from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homepage.views.home', name='home'),
    # url(r'^homepage/', include('homepage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Website urls
    url(r'^$', 'home.views.index', name='home'),
    #url(r'^home/', 'web.home.views.index'),
    #url(r'^tvseries/', 'web.tvseries.views.index'),
    #url(r'^about/', 'web.about.views.index'),
    #url(r'^contact/', 'web.contact.views.index'),
    #url(r'^links/', 'web.links.views.index'),
    #url(r'^myplaces/', ' web.myplaces.views.index'),
)
