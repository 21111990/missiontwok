from django import forms
from models import ClientDetailLog

class ClientDetailLogform(form.ModelForm):
    class Meta:
        model = ClientDetailLog
        fileds = ['Client_name','client_mobile','randid']

