from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):
    return render_to_response('about.html', RequestContext(request, {}))