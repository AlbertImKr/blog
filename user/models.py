from django.db import models


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(null=True, max_length=255, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    tistory = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
