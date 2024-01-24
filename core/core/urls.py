from core_apps.users.views import CustomUserDetailsView
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Writers Garden",
        default_version="v1",
        description="API endpoints for Writers Garden",
        contact=openapi.Contact(email="bikashpoudel4@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
    # USER + dj_rest_auth
    path("api/v1/auth/user/", CustomUserDetailsView.as_view(), name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/v1/auth/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    # Form own apps
    # Profiles app
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    # Articles app
    path("api/v1/articles/", include("core_apps.articles.urls")),
    # Ratings app
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
    # Bookmark app
    path("api/v1/bookmarks/", include("core_apps.bookmarks.urls")),
    # Responses app
    path("api/v1/responses/", include("core_apps.responses.urls")),
    # Search app
    path("api/v1/elastic/", include("core_apps.search.urls")),
]

"""For creating admin site customization"""
admin.site.site_header = "Writers Garden Admin"

admin.site.site_title = "Writers Garden Admin Portal"

admin.site.index_title = "Welcome to Writers Garden Portal"
