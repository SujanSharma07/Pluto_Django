from django.db import models
from main.models import User
# default --> null = False, blank = False

YEAR_IN_SCHOOL_CHOICES = (
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
    ('Graduate', 'Graduate'))

GENDERS = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]


class Citizenship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    DOB = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    c_no = models.PositiveIntegerField(unique=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)

    def __str__(self):
        return str(self.c_no)

    @property
    def address(self):
        return f"{self.district}, {self.state}-{self.country}"


class Room(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Language(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + ' | ' + str(self.origin)


class Gallery(models.Model):
    image = models.ImageField(upload_to="")


class Person(models.Model):
    year = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES,
                            max_length=150, default='Graduate')

    documents = models.FileField(upload_to='documents/', default='default.jpg')
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    desc = models.TextField()
    salary = models.FloatField()
    gender = models.CharField(max_length=50, choices=GENDERS, default='Male')
    is_verify = models.BooleanField(default=False)
    citizen = models.OneToOneField(
        Citizenship, on_delete=models.SET_NULL, null=True, blank=True)
    rooms = models.ForeignKey(
        Room, null=True, blank=True, on_delete=models.SET_NULL)
    language = models.ManyToManyField(Language)
    images = models.ManyToManyField(Gallery)
    #citizen = models.OneToOneField(Citizenship, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.id}"

    class Meta:
        ordering = ('-id', '-dob')


# age = models.IntegerField(default=18)
# age = models.IntegerField(null=True, blank=True)


""" 
# One to One
Citizenship
    full_name, DOB, father name, mothername, c_no, country, state, dirstrict
    vishal   

Person
fullname, email, contact, dob, address, profession, citizenship: 
                                                    {full_name, DOB, father name, mothername, c_no, country, state, dirstrict}




# One to Many
Room
    Room No, Type, Category

Person
fullname, email, contact, dob, address, profession, Room:
    {full_name, DOB, father name, mothername, c_no, country, state, dirstrict}


# Many to Many
language
    name, origin, country


Person
fullname, email, contact, dob, address, profession, Designation:
    {full_name, DOB, father name, mothername, c_no, country, state, dirstrict}



# Foreign Key
Reporter

Article """
