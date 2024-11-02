from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'info_acvut'
        managed = True
        verbose_name = 'info'
        verbose_name_plural = 'info'