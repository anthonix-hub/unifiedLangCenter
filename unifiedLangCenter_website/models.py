from django.db import models


class feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=500)
    feedback_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.name) + str(self.email) + str(self.message)

class Content(models.Model):
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    business_days = models.TextField(max_length=500)
    about =  models.TextField(max_length=500)
    mail =  models.EmailField(max_length=50)

    def __str__(self):
        return str(self.phone_number) + str(self.address) + str(self.business_days) + str(self.about) + str(self.mail)

class testimonie(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    write_up = models.TextField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.First_name) + str(self.Last_name) + str(self.write_up) + str(self.date_added)

class Post(models.Model):
    write_post = models.TextField(max_length=300, null=True, blank=True, )
    photo = models.ImageField(null=True,)
    date_written = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.write_post) + str(self.photo) + str(self.date_written)

class Gallery(models.Model):
    photo = models.ImageField(null=True,)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.photo) + str(self.date_uploaded)

class pactice(models.Model):
    words_to_translate = models.TextField(max_length=1000 )


