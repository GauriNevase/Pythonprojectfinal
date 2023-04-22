from django import forms
from .models import sos2
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class sos(forms.Form):
    La = forms.CharField(widget=forms.Textarea)
    Fp = forms.CharField(widget=forms.Textarea)
    Sn = forms.CharField(widget=forms.Textarea)
    Ws = forms.CharField(widget=forms.Textarea)
    Ca = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'La',
            'Fp',
            'Sn',
            'Ws',
            'Ca',
            Submit('submit','Submit',)
        )
        




class sosform(forms.ModelForm):

    class Meta:
        model = sos2
        fields = ('La',)