from . import views
from django.conf.urls import url


urlpatterns = [
                url(r'^$',views.index_view.as_view()),
                url(r'^user$',views.movies_view.as_view()),
                 url(r'^register$',views.register_view.as_view()),
    ]