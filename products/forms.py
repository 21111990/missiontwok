from django import forms
from models import ClientDetailLog

class ClientDetailLogform(forms.ModelForm):
    class Meta:
        model = ClientDetailLog
        fields = ['Client_name','client_mobile','randid']

    def index1(self):
        val1 = int(self.POST["userid"])
        val2 = str(self.POST["username"])
        val3 = int(self.POST["userMobile"])
        for instance in ClientDetailLog.objects.all():
            if instance.Client_name == val2 :
                raise forms.ValidationError('Already login')
        return val2
        ClientDetailLog_info = ClientDetailLog(Client_name=val2, client_mobile=val3, randid=val1)
        ClientDetailLog_info.save()
        return render(request, 'index.html',
                      {'userId1': val1, 'username': val2, 'usermobile': val3, 'UserDetails': UserDetails1,
                       'products': ShopProduct})