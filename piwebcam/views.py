from django.shortcuts import render
from django.http import HttpResponse
import picamera

camera = picamera.PiCamera()

def index(request):
    camera.capture("piwebcam/static/piwebcam/image.jpg")
    return render(request,
                  "piwebcam/index.html.jj2")
