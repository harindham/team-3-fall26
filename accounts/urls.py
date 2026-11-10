import secrets

from django.contrib.auth.views import LoginView
from django.urls import path

from accounts import views
from accounts.forms import LoginForm

app_name = "accounts"


class ProfileLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session["show_daily_deal_optin"] = True
        self.request.session["daily_deal_prompt_key"] = secrets.token_urlsafe(12)
        return response


urlpatterns = [
    path("location/", views.capture_location, name="capture_location"),
    path("profile/", views.profile, name="profile"),
    path("profile/<str:username>/", views.view_profile, name="view_profile"),
    path("signup/", views.signup, name="signup"),
    path("login/", ProfileLoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("verify/<str:uidb64>/<str:token>/", views.verify_email, name="verify_email"),
]
