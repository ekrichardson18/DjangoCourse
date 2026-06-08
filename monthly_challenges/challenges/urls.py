from django.urls import path

from . import views

# if request reaches first argument path, execute second argument function
# do not include project name because this is defined in project wide urls
urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    path("", views.monthly_challenges_home_page, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]