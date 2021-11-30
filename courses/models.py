from django.db import models
from django.contrib.auth.models import User
from django.db.models import constraints
from django.utils.text import slugify


# Create your models here.
# only stuff create and readonly
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="categories", blank=True, null=True)
    bg_image_url = models.URLField(max_length=254)

    def __str__(self):
        return self.name

# only stuff create and readonly


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="courses", blank=True, null=True)
    bg_image_url = models.URLField(max_length=254)

    def __str__(self):
        return self.name
# stuff and course teachers can create and readonly


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="lessons", blank=True, null=True)
    bg_image_url = models.URLField(max_length=254)

    def __str__(self):
        return self.name

# stuff and course teachers can create and course students and course teacher and stuff can read


class Post(models.Model):
    name = models.CharField(max_length=255, unique=True)
    text = models.TextField()

    slug = models.SlugField(blank=True, unique=True)

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="topics", blank=True, null=True)
    bg_image_url = models.URLField(max_length=254)

    created_date = models.DateField(auto_now_add=True)
    last_updated_date = models.DateField(auto_now=True)

    STATUS_CHOICES = (
        (1, "Publish"),
        (0, "Draft"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

# login user can create and readonly
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + self.post.name
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['user', 'post'], name="unique_like")
        ]

# login user can create and readonly
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=5000)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + self.post.name

# login user can create and readonly
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + self.post.name
