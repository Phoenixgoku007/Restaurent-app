from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from restaurant import views
from restaurant.views import logout_view
from django.contrib.auth import views as auth_views
from restaurant.views import signup
from accounts import views
from accounts.views import signup_view

from restaurant.views import (
    restaurant_list_view,
    restaurant_detail_view,
    add_review_view,
    edit_review_view,
    delete_review_view,
    add_bookmark_view,
    remove_bookmark_view,
    add_visit_view,
    remove_visit_view,
)

app_name='accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', restaurant_list_view, name='restaurant_list'),
    path('home', restaurant_list_view, name='restaurant_list'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('signup/', signup, name='signup'),
    path('accounts/profile/', views.profile_view, name='profile'), #throwing error 
    path('<int:id>/', restaurant_detail_view, name='restaurant_detail'),
    path('<int:id>/add_review/', add_review_view, name='add_review'),
    path('edit_review/<int:id>/', edit_review_view, name='edit_review'),
    path('delete_review/<int:id>/', delete_review_view, name='delete_review'),
    path('<int:id>/add_bookmark/', add_bookmark_view, name='add_bookmark'),
    path('remove_bookmark/<int:id>/', remove_bookmark_view, name='remove_bookmark'),
    path('<int:id>/add_visit/', add_visit_view, name='add_visit'),
    path('remove_visit/<int:id>/', remove_visit_view, name='remove_visit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
