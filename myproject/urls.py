"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from myapp import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    # url('^api/auth/', include('social_django.urls', namespace='social')),
    
    url(r'^results2/$',views.buy_search,name="buy_search"),
    url(r'^results1/$',views.sell_search,name="sell_search"),
    url(r'^addzone/(?P<id>[0-9]+)/$',views.addzone, name='zone'),
    url(r'^addround/(?P<id>[0-9]+)/$', views.addround, name='addround'),
    url(r'^addticket/(?P<id>[0-9]+)/$', views.addticket, name='addticket'),
    path('addconcert/', views.CreateConcertView.as_view(), name='addconcert'),
    path('oauth/', include('social_django.urls', namespace='social')), # in django2
    url(r'^login/$', auth_views.login, name='login'), 
    path('logout/',views.logout, name='logout'),   
    path('admin/', admin.site.urls),    
    path('home/', views.home, name='home'),
    path('sell/', views.sell, name='sell'),
    path('buy/', views.buy, name='buy'),
    url(r'^choosezone/(?P<id>[0-9]+)/$', views.choosezone, name='choosezone'),
    url(r'^ticket/(?P<id>[0-9]+)/$', views.ticket, name='ticket'),
    url(r'^contact/(?P<id>[0-9]+)/$', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^order/(?P<id>[0-9]+)/(?P<shipping>[0-9]+)/$', views.CreateOrder ,name="order"),
    path('editprofile/', views.update_profile, name='editprofile'),
    path('profile/', views.profile, name='profile'),
    url(r'^profile/(?P<id>[0-9]+)/$', views.view_profile, name='profile'),
    url(r'^soldout/(?P<id>[0-9]+)/$', views.change_soldout, name='soldout'),
    url(r'^onsell/(?P<id>[0-9]+)/$', views.change_onsell, name='onsell'),
    url(r'changetoread/(?P<id>[0-9]+)/$', views.changetoread, name='changetoread'),
    path('contactus/', views.contactus,name='contactus'),
    url(r'^vieworder/(?P<id>[0-9]+)/$', views.view_order, name='vieworder'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
