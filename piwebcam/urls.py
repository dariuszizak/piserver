from django.conf.urls import url, include
from piwebcam import views

app_name = "piwebcam"

urlpatterns = [url(r"^$", views.index, name="index")]
