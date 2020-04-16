from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

SOURCE_CHOICES = (
    ('WB','Website'),
    ('ADV','Advertisement'),
    ('FRND','Friend'),
)

class Document(models.Model):
    """Model definition for Document."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="exports")
    created_time = models.DateTimeField(auto_now_add=True)
    _type = models.CharField(max_length=100)
    source_type = models.CharField(
        choices=SOURCE_CHOICES, blank=True, null=True ,max_length=20)
    source_id = models.CharField(blank=True,null=True, max_length=50)
    input_meta_data = JSONField(default=dict,null=True,blank=True)

    class Meta:
        """Meta definition for Document."""

        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        """Unicode representation of Document."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Document."""
        return ('')

    # TODO: Define custom methods here
