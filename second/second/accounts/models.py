from django.db import models

# default --> null = False, blank = False

YEAR_IN_SCHOOL_CHOICES = [
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
    ('Graduate', 'Graduate')]


class Person(models.Model):
    year = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES,
                            max_length=150, default='Graduate')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    desc = models.TextField()
    salary = models.FloatField()
    is_verify = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.id}"


# age = models.IntegerField(default=18)
# age = models.IntegerField(null=True, blank=True)