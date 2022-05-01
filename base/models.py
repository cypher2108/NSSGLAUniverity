from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(verbose_name='date_created', auto_now_add=True)
    subject = models.TextField(max_length=300)
    email = models.EmailField(verbose_name="email",
                              max_length=100, unique=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    link = models.URLField(max_length=200)
    thumbnail = models.ImageField(upload_to='posts/%Y/%m/%d/')

    def __str__(self):
        return self.post_title


class Event(models.Model):
    event_title = models.CharField(max_length=150)
    date_of_event = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=150)
    link = models.URLField(max_length=200)
    thumbnail = models.ImageField(upload_to='events/%Y/%m/%d/')

    def __str__(self):
        return self.event_title


class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    link = models.URLField(max_length=200)
    thumbnail = models.ImageField(upload_to='blogs/%Y/%m/%d/')
    author = models.CharField(max_length=50)
    date_published = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.blog_title + " by " + self.author


class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_applied = models.DateTimeField(
        verbose_name='date_applied', auto_now_add=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="email",
                              max_length=100, unique=True)
    profile_picture = models.ImageField(
        null=True, upload_to='application/%Y/%m/%d/')
    designation = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    response = models.CharField(max_length=9, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], null=True, blank=True)

    def __str__(self):
        return self.first_name + " applied as: " + self.designation
