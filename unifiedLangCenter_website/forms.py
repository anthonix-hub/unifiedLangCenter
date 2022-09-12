from django import forms
from django.forms import ModelForm, models
from django.db.models import fields
from .models import testimonie,feedback,pactice


class feedbackForm(ModelForm):
    class Meta:
        model = feedback
        fields = (
            'name',
            'email',
            'message',
        )

class testimonialForm(ModelForm):
    class Meta:
        model = testimonie
        fields = (
            'write_up',
            'First_name',
            'Last_name',
        )


class pacticeForm(ModelForm):
    # body = forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Enter words to translate')}),label='' )
    class Meta:
        model = pactice
        fields = (
            'words_to_translate',
        )
