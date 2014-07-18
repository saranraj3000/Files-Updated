from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from julyapp import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'julyapp.views.homepage', name='home'),
    url(r'^mainpage$', 'julyapp.views.mainpage', name='new'),
    url(r'^hello$', 'julyapp.views.hello', name='hello'),
    url(r'^hello1$', 'julyapp.views.hello1', name='hello1'),
    url(r'^add$', 'julyapp.views.add', name='add'),
    url(r'^name$', 'julyapp.views.name', name='name'),
    url(r'^hello$', 'julyapp.views.hello', name='hello'),
    url(r'^hello1$', 'julyapp.views.hello1', name='hello1'),
    url(r'^namemodel$', 'julyapp.views.namemodel', name='namemodel'),
    url(r'^district$', 'julyapp.views.district', name='district'),
    url(r'^districtlist$', 'julyapp.views.districtlist', name='districtlist'),
    url(r'^usersignup$', 'julyapp.views.usersignup', name='usersignup'),
    url(r'^userlogin$', 'julyapp.views.userlogin', name='userlogin'),
    url(r'^userlogout$', 'julyapp.views.userlogout', name='userlogout'),
	url(r'^logincheck$', 'julyapp.views.logincheck', name='logincheck'),
	url(r'^notlogin$', 'julyapp.views.notlogin', name='notlogin'),
	url(r'^cookie$', 'julyapp.views.cookie', name='cookie'),
    url(r'^sarancookie$', 'julyapp.views.sarancookie', name='sarancookie'),
    url(r'^index123$', 'julyapp.views.index123', name='index123'),
    url(r'^session$', 'julyapp.views.session', name='session'),
#    url(r'^NameForm$', 'julyapp.views.NameForm', name='NameForm'),
    url(r'^get_name$', 'julyapp.views.get_name', name='get_name'),
#    url(r'^saransession$', 'julyapp.views.saransession', name='saransession'),
    
    # url(r'^register$', 'julyapp.views.register', name='register'),
    url(r'^list$', 'julyapp.views.list', name='list'),
    url(r'^edit/?(?P<id>\d+?)?/$', 'julyapp.views.edit', name='edit'),
    url(r'^delete/?(?P<id>\d+?)?/$', 'julyapp.views.delete', name='delete'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^adminlogin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()