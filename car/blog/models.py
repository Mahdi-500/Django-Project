from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import datetime

# Create your models here.

class SignUp(models.Model):

    class GenderChoices(models.TextChoices):
        FEMALE = "FE", ("Female")
        MALE = "M", ("Male")
        CORROSAN = 'CR', ("Corrosan")
    
    # ? user info
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    gender = models.CharField(choices=GenderChoices.choices, default=GenderChoices.MALE, max_length=2)

    # ? date info
    joined = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.user.username



class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Post(models.Model):

    class EngineChoices(models.TextChoices):
        V = 'V', ("V type")
        I = "i", ("inline")
        F = "F", ("Flat")
        B = "B", ("Boxer")
        W = "W", ("W type")
        R = "R", ("Rotary")

    class StatusChoices(models.TextChoices):
        DRAFT = "DR", ("Draft")
        ACCEPTED = "AC", ("Accept")
        REJECTED = "RJ", ("Rejected")

    class Published(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status=Post.StatusChoices.ACCEPTED)

    # ? customized manager
    objects = models.Manager()  # default manager
    Publish = Published()  # new manager

    # ? user info
    author = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='author')

    # ? post info
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    engine_type = models.CharField(choices=EngineChoices, default=EngineChoices.I, max_length=2)
    status = models.CharField(choices=StatusChoices, default=StatusChoices.DRAFT, max_length=2)
    slug = models.SlugField(max_length=100, null=True)
    reading_time = models.IntegerField(default=0)
    
    # ? date info
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "-created"
            ]
        
        indexes = [models.Index(fields=[
            'author'
            ])]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post detail", kwargs={"id":self.id})
    
    def __str__(self):
        return self.title


class Ticket(models.Model):

    class TicketType(models.TextChoices):
        SUGESSTION = "SG", ("Sugesstions")
        REPORT = "RE", ("Report")
        OTHER = "OT",("Other")

    # ? user info
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    # ? ticket details
    title = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=2, choices=TicketType, default=TicketType.SUGESSTION)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            '-created'
            ]
        

class Comment(models.Model):
        
    class StatusChoices(models.TextChoices):
        DARFT = "DR", ("Draft")
        REJECTED = "RJ", ("Rejected")
        ACCEPTED = "AC", ("Accepted")

    class Accepted(models.Manager):
            def get_queryset(self) -> models.QuerySet:
                return super().get_queryset().filter(status=Comment.StatusChoices.ACCEPTED)
    
    # ? new manager
    objects = models.Manager()  # default manager
    accepted = Accepted()  # new manager

    # ? post info
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")

    # ? user info
    author = models.ForeignKey(SignUp, on_delete=models.CASCADE)

    # ? comment info
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=StatusChoices, default=StatusChoices.DARFT)

    class Meta:
        ordering = [
            '-created'
        ]


# todo changes the saving path
def post_images_path(instance, filename):
    return 'post_images/{0}/{1}/{2}/{3}/{4}/{5}'.format(instance.post.author.username, datetime.datetime.now().year,
                                                datetime.datetime.now().month, instance.post.title, instance.post.id, filename)


class Image(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")

    # ? saving image file
    image_file = ResizedImageField(upload_to=post_images_path, quality=80, force_format="PNG", size=[500, 500])

    # ? image info
    title = models.CharField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=[
            "-title"
        ]
        indexes=[
            models.Index(fields=['date_created'])
        ]
    
    def __str__(self):
        return self.title if self.title else Post.Publish.get(id=self.post.id).title
    
@receiver(post_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    if instance.image_file:
        instance.image_file.delete(False)
