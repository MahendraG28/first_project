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

#  <h1> HI </h1> 
# <h4>this is my first deployment</h4>
# <p>topgrep</p>