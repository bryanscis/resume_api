from django.db import models

class Comments(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: my email is {self.email} and I said "{self.comment}" '