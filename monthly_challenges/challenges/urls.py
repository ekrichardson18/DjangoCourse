from django.urls import path

from . import views

# if request reaches first argument path, execute second argument function
# do not include project name because this is defined in project wide urls
urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    path("<month>", views.monthly_challenge)
]