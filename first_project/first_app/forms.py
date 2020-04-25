from django import forms
from django.core import validators
from first_app.models import User

def check_for_letter(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("Name should start with z")

class NewUserForm(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'

class FormName(forms.Form):
    #name=forms.CharField(validators=[check_for_letter])
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter Mail again")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vemail=all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Mails did not match")
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Catched a Bot!")
    #     return botcatcher
