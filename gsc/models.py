from django.db import models


class user(models.Model):
    email = models.CharField(max_length=52)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=16)
    org_name = models.TextField()

    # def __str__(self):
    #    return self.email


class users(models.Model):
    email = models.CharField(max_length=52)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=16)
    org_name = models.TextField()


class website(models.Model):
    web_name = models.CharField(max_length=80)
    website_url = models.TextField()
    user_id = models.IntegerField()
