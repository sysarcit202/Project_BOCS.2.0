from django.db import models

class User(models.Model):
    UempId = models.CharField(max_length=20)
    Uname = models.CharField(max_length=20)
    Uemail = models.EmailField()
    UjRole = models.CharField(max_length=20)
    UidNum = models.CharField(max_length=20)
    Upass = models.CharField(max_length=20)
    UrPass = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'