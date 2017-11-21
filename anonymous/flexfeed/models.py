from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    description = models.CharField(max_length=100, help_text="Enter a post description")
    link = models.URLField(max_length=20000, default='')
    site_Choices = (
        ('IG', 'Instagram'),
        ('TWT', 'Twitter'),
        ('FB', 'Facebook'),
    )

    site = models.CharField(max_length=3, choices=site_Choices, blank=True, default='FB', help_text='Choose the site this post is on')


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.description


class Stock(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    company = models.CharField(max_length=50, help_text="The company that has this stock value.")
    value = models.DecimalField(help_text="The value of the stock.",max_digits=5,decimal_places=2)
    trend = models.IntegerField(help_text="0 if trending down, 1 if trending up.")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.company + " " + str(self.value) + " " + str(self.trend)


class Category(models.Model):
    """
    Model representing a category
    """

    name = models.CharField(max_length = 150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Member(models.Model):
    """
    Model representing a member.
    """
    name = models.CharField(max_length=100)
    profile_picture = models.URLField(max_length=20000, default='')
    sm_links = models.URLField()
    stock = models.ForeignKey(Stock, help_text="Select a stock for this member", blank=True, null=True)
    post = models.ManyToManyField(Post, help_text="Select a post for this member")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.name


class Group(models.Model):
    """
    Model representing a group
    """
    members = models.ManyToManyField(Member, help_text="Select a member")
    subscribers = models.IntegerField()
    views = models.IntegerField()
    popularity = models.IntegerField()
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, help_text="Select a category")
    picture = models.URLField(max_length=20000, default='')

    def __str__(self):
        """r
        String for representing the group object
        """
        return self.name


class Profile(models.Model):
    """
    A class which defines a Profile.
    """
    import uuid  # Required for unique book instances
    from django import forms

    # fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField()
    groups = models.ManyToManyField(Group, help_text="Select a group")

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
