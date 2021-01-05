from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    logger.debug("Log statement with key")
    return HttpResponse("Hello, world.You're at the polls index.")
