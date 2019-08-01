def get_utorid(request):
    """
    Returns utorid from request object.
    """
    return request.environ['utorid']
