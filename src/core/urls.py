from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from rest_auth.registration.views import SocialAccountListView
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("auth/social/google", views.GoogleLogin.as_view(), name="google_rest_login"),
    path("auth/social/facebook", views.GoogleLogin.as_view(), name="fb_rest_login"),
    path("auth/social/github", views.GithubLogin.as_view(), name="gh_rest_login"),
    path("auth/social/list", SocialAccountListView.as_view(), name="social_list"),
    path("auth/", include("rest_auth.urls")),
    path("auth/token/refresh", refresh_jwt_token, name="refresh_jwt"),
    path("auth/token/verify", verify_jwt_token, name="verify_jwt"),
    path("auth/registration/", include("rest_auth.registration.urls")),
    path("auth/profile", views.UpdateProfile.as_view(), name="update_profile"),
    # Used by allauth to send the "verification email sent" response to client
    path(
        "auth/account-email-verification-sent",
        TemplateView.as_view(),
        name="account_email_verification_sent",
    ),
]

# Used for social auth development
if settings.DEBUG or settings.TESTING:
    urlpatterns += [
        path("dev/", include("allauth.account.urls")),
        path("dev/", include("allauth.socialaccount.providers.google.urls")),
        path("dev/", include("allauth.socialaccount.providers.facebook.urls")),
        path("dev/", include("allauth.socialaccount.providers.github.urls")),
        path("dev/social/", include("allauth.socialaccount.urls")),
    ]
