from django.shortcuts import render
from django.views import View
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .helpers import get_utorid, generateRedirectURL, generateSessionId
from .models import Service, Mask

# Create your views here.

class RedirectView(View):

    def get(self, request):
        """
        Redirect request with parameters.
        """
        try:
            # user authentication
            utorid = get_utorid(request)

            # extract url parameters
            service_name = request.GET.__getitem__('service')
            params = request.GET.get('params')

            # query for required info
            service = Service.objects.get(name=service_name)
            usr = Mask.objects.get(userId=utorid, service=service)

            host = service.host
            # use default service parameters if none were provided in the request
            if not params:
                params = service.params

	    # get random session id
            sessionId = generateSessionId()
			
            # add additional parameters to params
            params += "&usr=" + usr.pseudoId
            params += "&sid=" + sessionId

                                          
            return HttpResponseRedirect(generateRedirectURL(host, params))

        except KeyError:
            return HttpResponseBadRequest("<h1>An error occured while processing your request</h1>") 
        except ObjectDoesNotExist:
            return HttpResponseBadRequest("<h1>An error occured while processing your request</h1>")
