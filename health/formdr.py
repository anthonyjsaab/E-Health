from django import forms
from .models import DoctorInfo


# creating a form
class drform(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = DoctorInfo

        # specify fields to be used
        fields = [
            "firstname",
            "lastname",
            "password",
            "confirmation",
            "emailDr",
            "specialization",
            "hospital"
        ]
