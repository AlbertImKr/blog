from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="posts"
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="posts"
    )
    image = models.OneToOneField(
        "image.Image", on_delete=models.SET_NULL, related_name="post", null=True
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
