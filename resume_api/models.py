from django.db import models
from django.contrib.postgres.fields import ArrayField

class Comments(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: my email is {self.email} and I said "{self.comment}" at {self.created_at} '
    
class Projects(models.Model):
    name = models.CharField(max_length=50)
    description = ArrayField(models.CharField(max_length=500))
    stack = ArrayField(models.CharField(max_length=70))

    def __str__(self):
        return f'{self.name}: {self.description} with stack: {self.stack}'
    
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    time_at_company = models.CharField(max_length=100)
    responsibilities = ArrayField(models.CharField(max_length=500))

    def __str__(self):
        return f'I worked at {self.company} as a {self.title} from {self.time_at_company}. My responsibilities were {self.responsibilities}.'
    
class Contact(models.Model):
    platform = models.CharField(max_length=100)
    information = models.CharField(max_length=100)

    def __str__(self):
        return f'My {self.platform} is {self.information}'
    
class Route(models.Model):
    route = models.CharField(max_length=100)
    information = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.route} : {self.information}'