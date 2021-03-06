from django.db import models

class Image(models.Model):
    """
    This class defines the Image model. Each sandbox should be created with an
    Image as a base. Each Image should be have a valid counterpart to every
    Docker server connected to OpenDevelop
    """
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    description = models.TextField()
    url = models.URLField(max_length=64, blank=True, null=True, default='')
    docker_image_name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name
