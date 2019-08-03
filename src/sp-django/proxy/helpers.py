import uuid
from random import SystemRandom
from string import ascii_uppercase, digits

def get_utorid(request):
    """
    Returns utorid from request object.
    :return: (string)
    """
    return request.environ['utorid']

def generateRedirectURL(host, params):
    """
    Computes the redirect url in the specified format.
    :return: (string)
    """
    return "{}?{}".format(host, params)

def generateSessionId():
    """
    Returns a random 5 character string consisting of numbers [0-9] and 
    uppercase letters [A-Z].
    :return: random 5 char (string) 
    """
    return ''.join(SystemRandom().choice(ascii_uppercase + digits) 
           for _ in range(5))
