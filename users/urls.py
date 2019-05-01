from django.conf.urls import url
from django.views.generic.base import TemplateView
# from . import views

urlpatterns = [
    url(r'^signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
]