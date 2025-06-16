from .models import Super
from django import forms


Gender = [
    ('M','Male'),
    ('F','Female'),
    ('O','Others'),
]


ODISHA_CITIES = [
    ("angul", "Angul"),
    ("balangir", "Balangir"),
    ("balasore", "Balasore"),
    ("bargarh", "Bargarh"),
    ("baripada", "Baripada"),
    ("berhampur", "Berhampur"),
    ("bhadrak", "Bhadrak"),
    ("bhawanipatna", "Bhawanipatna"),
    ("bhubaneswar", "Bhubaneswar"),
    ("boudh", "Boudh"),
    ("cuttack", "Cuttack"),
    ("deogarh", "Deogarh"),
    ("dhenkanal", "Dhenkanal"),
    ("gajapati", "Gajapati"),
    ("ganjam", "Ganjam"),
    ("jagatsinghpur", "Jagatsinghpur"),
    ("jajpur", "Jajpur"),
    ("jharsuguda", "Jharsuguda"),
    ("kalahandi", "Kalahandi"),
    ("kandhamal", "Kandhamal"),
    ("kendrapara", "Kendrapara"),
    ("keonjhar", "Keonjhar"),
    ("khordha", "Khordha"),
    ("koraput", "Koraput"),
    ("malkangiri", "Malkangiri"),
    ("mayurbhanj", "Mayurbhanj"),
    ("nabarangpur", "Nabarangpur"),
    ("nayagarh", "Nayagarh"),
    ("nuapada", "Nuapada"),
    ("paradip", "Paradip"),
    ("puri", "Puri"),
    ("rayagada", "Rayagada"),
    ("rourkela", "Rourkela"),
    ("sambalpur", "Sambalpur"),
    ("sonpur", "Sonepur"),
    ("sundargarh", "Sundargarh"),
]




class SuperForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices = Gender,
        widget = forms.RadioSelect
    )
    city = forms.ChoiceField(
        choices = ODISHA_CITIES
    )
    class Meta:  
        model = Super
        fields = [
            'name','email','gender','mobile','dob','state','city','pin','profile_image','file'
        ]
        labels = {
            'name':'FullName',
            'email':'Email',
            'gender':'Gender',
            'mobile':'Mobile',
            'dob':'DateofBirth',
            'state':'State',
            'city':'City',
            'pin':'Pincode',

        }

        help_texts = {
            'profile_image':'optional:You can Upload your beutiful image of yours',
            'file': 'optional:upload any file'
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker','type':'date'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
        }