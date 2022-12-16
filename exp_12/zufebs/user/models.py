from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class AbstractUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(
#         _('username'),
#         max_length=150,
#         unique=True,
#         …… ,
#     )
#     first_name = models.CharField( …… )
#     last_name = models.CharField( …… )
#     email = models.EmailField( …… )
#     is_staff = models.BooleanField( …… )
#     is_active = models.BooleanField( …… )
#     date_joined = models.DateTimeField( …… )


def check_uname(uname):
    user = User.objects.filter(username=uname)
    return user.exists()

def add_user(uname, upass, uemail):
    user = User.objects.create_user(username=uname, password=upass, email=uemail, is_staff=False)
    user.save()
