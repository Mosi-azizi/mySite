from django.db import models
import  uuid
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    intro = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(default='profiles/user-default.jpg', null=True, blank=True, upload_to='profiles/')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=200, blank=True,null=True)
    skype = models.CharField(max_length=200, blank=True, null=True)
    microsoft_team = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True,null=True)
    phone_number = models.CharField(max_length=200,blank=True,null=True)
    mobile_number = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    level_experience = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Education(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.degree)

class Employment(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    employer = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.job_title)

class Message(models.Model):
    name = models.CharField(max_length=200, null=True , blank=True, verbose_name='Name')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='E-mail')
    subject = models.CharField(max_length=200, null=True, blank=True,verbose_name='Subject')
    body = models.TextField(verbose_name='Your Message')
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.subject




