from django.shortcuts import render
from django.views import View
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .helpers import get_utorid
from .models import Service, Mask

# Create your views here.

class RedirectView(View):

    def get(self, request):
        """
        Redirect request with parameters.
        """
        try:
            service_name = request.GET.get('service')
            params = request.GET.get('params', None)
            utorid = get_utorid(request)

            service = Service.objects.get(name=service_name)
            host = service.host
            if not params:
                params = service.params

            usr = Mask.objects.get(userId=utorid, service=service).anonId

            url = host + "?" + params + "&usr=" + usr

            return HttpResponseRedirect(url)

        except KeyError:
            return HttpResponseBadRequest() 
        except ObjectDoesNotExist:
            return HttpResponseBadRequest()
