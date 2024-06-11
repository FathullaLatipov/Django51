from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from products.views import HomePage, product_page, search
# ИМПОРТ!!
from users.views import register_view, login_view, profile_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view()),
    path('search', search),
    path('products/<int:id>', product_page),
    path('signup', register_view),
    path('login', login_view),
    path('profile', profile_view),
    path('logout', logout_view)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
