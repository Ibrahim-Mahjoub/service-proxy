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
