from django.shortcuts import render
from django.views import View
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .helpers import get_utorid, computeRedirectURL, createSessionId
from .models import Service, Mask

# Create your views here.

class RedirectView(View):

    def get(self, request):
        """
        Redirect request with parameters.
        """
        try:
            # extract url parameters
            service_name = request.GET.__getitem__('service')
            params = request.GET.get('params')
            utorid = get_utorid(request)

            # query for required info
            service = Service.objects.get(name=service_name)
            host = service.host

            # use default service parameters if none were provided in the request
            if not params:
                params = service.params

            usr = Mask.objects.get(userId=utorid, service=service)

            sessionId = createSessionId()
			
            # add user parameter to params
            params += "&usr=" + usr.anonId
            params += "&sid=" + sessionId

                                          
            return HttpResponseRedirect(computeRedirectURL(host, params))

        except KeyError:
            return HttpResponseBadRequest("<h1>An error occured while processing your request</h1>") 
        except ObjectDoesNotExist:
            return HttpResponseBadRequest("<h1>An error occured while processing your request</h1>")
