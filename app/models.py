from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def valid(value):
    if len(str(value)) != 6:
        raise ValidationError('the pin must be 6')


STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
]

Gender = [
    ('M','Male'),
    ('F','Female'),
    ('O','Others'),
]



# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length =100)
    email = models.EmailField()
    gender = models.CharField(choices=Gender,max_length=10)
    mobile = models.CharField(max_length=10,
                              help_text='enter 10 digit mobile number',
                              validators=[RegexValidator(regex=r'^[6-9]\d{9}$')]
                              )
    dob = models.DateField(auto_now=False,auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    city = models.CharField(max_length=50)
    pin = models.PositiveIntegerField(
        validators=[valid],
        help_text='enter 6 digit pin',)
    profile_image = models.ImageField(upload_to='profileimg',blank=True)
    file = models.FileField(upload_to='doc',blank=True)
