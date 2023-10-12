from django.urls import path
from django.views.generic import TemplateView


app_name = "pages"

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home/index.html"), name="home"),
    path("contact", TemplateView.as_view(template_name="pages/contact/index.html"), name="contact"),
    path("events", TemplateView.as_view(template_name="pages/events/index.html"), name="events")
    
    
]