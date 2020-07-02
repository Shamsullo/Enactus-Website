from django.db import models

# Create your models here.


class Welcome(models.Model):
    video = models.FileField(upload_to='videos/', blank=True)
    photo = models.ImageField()
    text_under_welcome = models.CharField(max_length=100)

    def __str__(self):
        return 'Welcoming Page'


class AboutEnactus(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    # photo = models.ImageField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallerry/')
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption


class Projects(models.Model):
    name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=200)
    description = models.TextField()
    photo1 = models.ImageField(upload_to='project')
    photo2 = models.ImageField(upload_to='project', blank=True)

    def __str__(self):
        return self.name


class AcademicAdvisors(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='Our Team')
    email = models.CharField(max_length=150, blank=True)
    linkedin = models.CharField(max_length=150, blank=True)
    fb = models.CharField(max_length=150, blank=True)
    insta = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.f_name + " " + self.l_name


class Contact(models.Model):
    address = models.CharField(max_length=150)
    phone_num1 = models.CharField(max_length=30)
    phone_num2 = models.CharField(max_length=30, blank=True)
    phone_num3 = models.CharField(max_length=30, blank=True)
    insta_link = models.CharField(max_length=150)
    fb_link = models.CharField(max_length=150)

    def __str__(self):
        return "Our Contact"


class Partners(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='Partners')
    web_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
