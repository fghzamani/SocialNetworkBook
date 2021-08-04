from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [('F', 'female'), ('M', 'male')]
    first_name = models.CharField('first name', max_length=100, null=True)
    last_name = models.CharField('last name', max_length=100, null=True, blank=True)
    username = models.CharField('username', max_length=100, null=False, unique=True)
    # username = models.CharField('username', max_length=100, null=False, primary_key=True)
    profile = models.TextField('profile', max_length=150, null=True, blank=True)
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES, default='F')
    phone_number = models.CharField('phone number', max_length=11, blank=True)
    biography = models.CharField('biography', max_length=50, null=True)
    country = models.CharField('country', max_length=20, null=True)
    website = models.URLField('website')
    email = models.EmailField('email')
    registered = models.DateTimeField('register date', auto_now_add=True)
    updated = models.DateTimeField('update date', auto_now=True, null=True)
    credit = models.IntegerField('credit', default=20)
    friends = models.ManyToManyField("Profile", blank=True, related_name='my_friends')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def delete_user(self):
        deleted_user = f"user '{self.first_name} {self.last_name}' has been deleted"
        self.delete()
        return deleted_user

    def update_credit(self, amount):
        self.credit += amount
        self.save()

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def get_books(self):
        return self.owner.all()

    def get_books_no(self):
        return self.owner.all().count()

    def __str__(self):
        return f'{self.username} registered at {self.registered}'


class Relationship(models.Model):
    STATUS_CHOICE = [('R', 'requested'), ('A', 'accepted')]
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices=STATUS_CHOICE, default='R')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.sender}, {self.receiver}, {self.status}'
