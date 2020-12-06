from .models import Call
from django import forms


class RequestForm(forms.ModelForm):
    req_date = forms.CharField(widget=forms.DateTimeInput(format='%d-%m-%Y %H:%M')) 
    url = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
    class Meta:
        model = Call
        fields = ['url', 'req_date']
