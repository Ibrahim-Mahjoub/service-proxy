from django.db import models

# Create your models here.

class Service(models.Model):
    """
    The service being requested.
    """
    # name of service
    name = models.TextField()
    # service url host
    host = models.TextField()
    # url formatted string of default parameters
    params = models.TextField()

class Mask(models.Model):
    """
    A mask that maps the authenticated user's id to it's pseudonymous
    service registered id.
    """
    # authenticated user's id
    userId = models.TextField()
    # the pseudonymous service registered id
    anonId = models.TextField()
    # the service the mask belongs to
    service = models.ForeignKey(Service, on_delete=models.CASCADE, 
                               related_name='mask')

    class Meta:
        unique_together = [['userId', 'service'], ['anonId', 'service']]
