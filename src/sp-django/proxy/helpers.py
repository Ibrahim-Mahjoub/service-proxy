from random import SystemRandom
from string import ascii_uppercase, digits
import logging
from django.utils.timezone import localtime

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

def log(msg, logger):
    """
    Logs message, msg, to the appropriate logger.
   
    :param msg: log message (string)
    :param logger: logger name (string)
    """
    logger = logging.getLogger(logger)
    logger.info(str(localtime()) + " | " + msg)

def logException(msg, logger):
    """
    Logs message, msg, to the appropriate logger along with a stacktrace
    of the exception.

    :param msg: log message (string)
    :param logger: logger name (string)
    """
    logger = logging.getLogger(logger)
    logger.exception(str(localtime()) + " | " + msg)
