import uuid

def get_utorid(request):
    """
    Returns utorid from request object.
    """
    return request.environ['utorid']

def computeRedirectURL(host, params):
    """
    Computes the redirect url in the specified format.
    """
    return "{}?{}".format(host, params)

def createSessionId():
    """
    Computes a session id for each user request.
    """
    return uuid.uuid4().hex
