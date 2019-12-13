import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser

# class PostCity(models.Model):
#     city = models.CharField(max_length=50)


################# auto generated template classes below #####################

# Custom User class which extends built-in User. Presently, just adds a "bio"
# and a gravatar method. Feel free to add your own new fields here!

class User(AbstractUser):

    bio = models.TextField()
    phone = models.CharField(max_length=20, blank=True)

    def gravatar(self, size=None):
        GRAVATAR_URL = 'https://gravatar.com/avatar/%s?d=identicon%s'
        email = str(self.email).strip().lower()
        digest = hashlib.md5(email.encode('utf-8')).hexdigest()

        if size:
            size_str = '&s=%i' % size
        else:
            size_str = ''

        return GRAVATAR_URL % (digest, size_str)


class Location(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    city = models.CharField(max_length=160)
    us_state = models.CharField(max_length=2, blank=True)
    country = models.CharField(max_length=160, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)