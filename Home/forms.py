from django.forms import ModelForm, DateField
from .models import FormModel
from django.conf import settings
from django.contrib.auth.decorators import login_required


class ModelDetailsForms(ModelForm):

    dob = DateField(input_formats=settings.DATE_INPUT_FORMATS,label="Date of Birth (DD/MM/YYYY)", help_text="Sample Input: 15/06/1996")

    class Meta:
        model = FormModel
        exclude= ["user"]
        
