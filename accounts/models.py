from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  

#So what is happening is when the User model is saved, a signal is fired called
    # create_profile which creates a Profile instance with a foreign key
        # pointing to the instance of the user. 
            #The other method save_profile just saves the instance.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    #receiver – The function who receives the signal and does something. 
    #sender – Sends the signal
    #created — Checks whether the model is created or not
    #instance — created model instance
    #**kwargs –wildcard keyword arguments