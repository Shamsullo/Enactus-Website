from django.db import models

# Create your models here.


class Welcome(models.Model):
    photo = models.ImageField()
    text = models.TextField()


class AboutEnactus(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.name


class AcademicAdvisors(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    photo = models.ImageField()
    position = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)

    def __str__(self):
        return self.f_name + " " + self.l_name


class Contact(models.Model):
    phone_num1 = models.CharField(max_length=30)
    phone_num2 = models.CharField(max_length=30)
    phone_num3 = models.CharField(max_length=30)
    insta_link = models.CharField(max_length=150)
    fb_link = models.CharField(max_length=150)

    def __str__(self):
        return "Our Contact"


class Partners(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField()
    web_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField()
