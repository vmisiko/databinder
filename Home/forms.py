from django.forms import ModelForm, DateField
from .models import FormModel
from django.conf import settings
from django.contrib.auth.decorators import login_required


class ModelDetailsForms(ModelForm):

    dob = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = FormModel
        exclude= ["user"]
        help_texts = {
            'dob': 'Sample Input: 27/08/1977',
        }

        labels = {
            "dob":"Date of Birth (DD/MM/YYYY)",
        }
