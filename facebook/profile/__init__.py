from django.db import models
from facebook.models import Base
from django.template.defaultfilters import slugify

class Profile(Base):
    """ Base Class for user, group, page, event and application. """
    id = models.BigIntegerField(primary_key=True, unique=True, help_text=_('The ID is the facebook page ID'))
    _name = models.CharField(max_length=200, blank=True, null=True)
    _link = models.URLField(max_length=255, verify_exists=False, blank=True, null=True, verify_exists=False)
    _picture = models.URLField(max_length=500, blank=True, null=True, verify_exists=False, help_text=_('Cached picture of the page'))
    _pic_square = models.URLField(max_length=500, blank=True, null=True, verify_exists=False, editable=False)
    _pic_small = models.URLField(max_length=500, blank=True, null=True, verify_exists=False, editable=False)
    _pic_large = models.URLField(max_length=500, blank=True, null=True, verify_exists=False, editable=False)
    _pic_crop = models.URLField(max_length=500, blank=True, null=True, verify_exists=False, editable=False)
    
    class Meta:
        abstract = True
    
    @property
    def _username(self):
        return self.slug
    
    @_username.setter
    def _username(self, name):
        self.slug = slugify(name)