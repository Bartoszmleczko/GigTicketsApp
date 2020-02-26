"""bilety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings # new
from django.urls import path, include,re_path # new
from django.conf.urls.static import static # new
from django.contrib.auth.decorators import login_required, permission_required
from zespol import views
from zespol import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('bands', views.bands, name='bands'),
    path('concerts', views.concerts, name='concerts'),
    path('clubs', views.clubs, name='clubs'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup,name='signup'),
    path('cart',views.cart,name='cart'),
    path('concerts/<int:pk>',login_required(views.ConcertDetail.as_view()),name='concert-detail'),
    path('thanks/<int:concert_id>',views.thanks,name='thanks'),
    path('delete/<int:ticket_id>',views.delete,name='delete_ticket'),
    path('buy/<int:ticket_id>',views.buy,name='buy_ticket'),
    path('deleteall',views.deleteall,name="delete_all"),
    path('buyall',views.buyall,name="buy_all"),
    path('profile',views.profile,name="profile"),
    path('profile-update',views.update_profile,name='profile_update'),
    path('clubs/<int:club_id>',views.club_details,name='club_details'),
    path('bands/<int:band_id>',views.band_details,name='band_details'),
    # path('^delete/(?P<pk>\d+)/$', login_required(views.PostDelete.as_view()),name='entry_delete')
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
