from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class BuildPost(models.Model):
    """
    Modeel to store a single build post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, default="", null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="build_posts"
    )
    #image = CloudinaryField('image', default='placeholder')
    #image_alt = models.CharField(
    #   max_length=100, default="",
    #   null=False, blank=False
    #)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    """
    Model to store a single comment entry related to :model:`auth.User`
    and :model:`build_dream.BuildPost`. Needs to be approved
    """
    build_post = models.ForeignKey(BuildPost, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    comment_title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"