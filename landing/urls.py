from django.conf.urls import url

from landing.views import LandingView

urlpatterns = [
    url(
        regex  = r"$",
        view = LandingView.as_view(),
        name = "landing_view",
        ),
]
