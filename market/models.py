from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        '''Create and save a user with the given email, and
        password.
        '''
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False,
    )

    # All these field declarations are copied as-is
    # from `AbstractUser`
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into '
            'this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be '
            'treated as active. Unselect this instead '
            'of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now,
    )

    # Add additional fields here if needed

    objects = UserManager()

    USERNAME_FIELD = 'email'



class Item(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def post(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title