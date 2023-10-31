# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse

# def hello(request):
#     text = """<h1>Hello, Welcome to my App!</h1>"""
#     return HttpResponse(text)

from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)


def hello(request):
    logger.info('Basic Logging')
    logger.warning('Warning')
    logger.error('Error message')
    text = """<h1>Hello, Welcome to my App!</h1>"""
    return HttpResponse(text)
