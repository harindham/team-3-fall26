from urllib.parse import urlencode

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import path, reverse

from accounts import views
from accounts.forms import LoginForm

app_name = "accounts"


class ProfileLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def form_valid(self, form):
        response = super().form_valid(form)
        capture_url = reverse("accounts:capture_location")
        return redirect(f"{capture_url}?{urlencode({'next': response.url})}")


urlpatterns = [
    path("location/", views.capture_location, name="capture_location"),
    path("profile/", views.profile, name="profile"),
    path("profile/<str:username>/", views.view_profile, name="view_profile"),
    path("signup/", views.signup, name="signup"),
    path("login/", ProfileLoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("verify/<str:uidb64>/<str:token>/", views.verify_email, name="verify_email"),
]
