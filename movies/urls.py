from . import views
from django.conf.urls import url


urlpatterns = [
                url(r'^/',views.movies_view.as_view()),
    ]