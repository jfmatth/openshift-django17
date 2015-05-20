from django.views.generic import View
from django.http import HttpResponse
from django import get_version


class Index(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Running Django ' + str(get_version()) + " on OpenShift")
