# Copyright (C) 2021-2022 Intel Corporation
# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path, re_path
from django.conf import settings
from django.urls.conf import include
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView,)
from dj_rest_auth.registration.views import (
    VerifyEmailView, ResendEmailVerificationView
)
from allauth.account.views import EmailVerificationSentView, ConfirmEmailView
from allauth.account import app_settings as allauth_settings
from cvat.apps.iam.views import SigningView, RegisterViewEx
from django.views.generic import TemplateView

urlpatterns = [
    path('login', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    path('logout', LogoutView.as_view(), name='rest_logout'),
    path('password/change', PasswordChangeView.as_view(), name='rest_password_change'),
    path('signing', SigningView.as_view(), name='rest_signing')
]

if settings.IAM_TYPE == 'BASIC':
    urlpatterns += [
        # URLs that do not require a session or valid token
        path('password/reset', PasswordResetView.as_view(), name='rest_password_reset'),
        path('password/reset/confirm', PasswordResetConfirmView.as_view(),
            name='rest_password_reset_confirm'),
        re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
            TemplateView.as_view(template_name="password_reset_confirm.html"),
            name='password_reset_confirm'),

    ]

    if getattr(settings, 'REST_USE_JWT', False):
        from rest_framework_simplejwt.views import TokenVerifyView

        from dj_rest_auth.jwt_auth import get_refresh_view

        urlpatterns += [
            path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
            path('token/refresh', get_refresh_view().as_view(), name='token_refresh'),
        ]

    if getattr(settings, 'IAM_REGISTRATION_ENABLED', True):
        urlpatterns += [
            path('register', RegisterViewEx.as_view(), name='rest_register'),
        ]

        if allauth_settings.EMAIL_VERIFICATION != allauth_settings.EmailVerificationMethod.NONE:
            urlpatterns += [
                path('verify-email', VerifyEmailView.as_view(), name='rest_verify_email'),
                path('resend-email', ResendEmailVerificationView.as_view(),
                    name="rest_resend_email"),

                # This url is used by django-allauth and empty TemplateView is
                # defined just to allow reverse() call inside app, for example when email
                # with verification link is being sent, then it's required to render email
                # content.

                # account_confirm_email - You should override this view to handle it in
                # your API client somehow and then, send post to /verify-email/ endpoint
                # with proper key.
                # If you don't want to use API on that step, then just use ConfirmEmailView
                # view from:
                # django-allauth https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py
                re_path(
                    r'^account-confirm-email/(?P<key>[-:\w]+)$', TemplateView.as_view(),
                    name='account_confirm_email',
                ),
                path(
                    'account-email-verification-sent', TemplateView.as_view(),
                    name='account_email_verification_sent',
                ),
            ]

urlpatterns = [path('auth/', include(urlpatterns))]
