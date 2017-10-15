from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.core.urlresolvers import reverse
class CustomUserManger(BaseUserManager):
    def _create_user(self,email,password,is_staff,is_superuser,**extra_fields):

        now = datetime.now()
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,
                            is_staff=is_staff,
                            is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self,email,password):
        return self._create_user(email,password,False,False)

    def create_superuser(self,email,password=None,**extra_fields):
        return self._create_user(email,password,True,True,**extra_fields)
    
class CustomUser(AbstractBaseUser):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    movies_list =ArrayField(models.TextField(),null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManger()

    def get_full_name(self):
        return self.first_name + " "+self.last_name

    def get_short_name(self):
        return self.first_name
   
    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})