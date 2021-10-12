from django.db import models
from account.models import Account


def get_profile_image_filepath(self, filename):
	return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():
	return "default.png"

class Teams(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    team_id = models.AutoField(primary_key=True)
    team_name = models.TextField(blank=True, null=True)
    leader_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    team_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)

    # Metadata
    class Meta:
        ordering = ['-team_id']
        verbose_name_plural = "Teams"



class TeamMembers(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    team_id =    models.ForeignKey(Teams, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    status =  models.BooleanField(default=True)
    last_updated = models.DateTimeField(verbose_name='date updated', auto_now_add=True)

    # Metadata
    class Meta:
        ordering = ['-team_id']
        verbose_name_plural = "Team Members"