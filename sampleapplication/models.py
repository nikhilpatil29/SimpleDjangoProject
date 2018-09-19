from django.db import models

class UserInfo(models.Model):
    # id = models.IntegerField(primary_key=True,auto_created=)
    username = models.CharField(max_length=20)
    emailid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


