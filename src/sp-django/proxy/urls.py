from django.conf.urls import url
from . import views

app_name = 'proxy'
urlpatterns = [
    url(r'^$', views.RedirectView.as_view()),
]
