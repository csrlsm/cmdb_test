from django import forms
from models import ServerList,DeviceList

class add_serverform(forms.ModelForm):
    class Meta:
        model = ServerList
        exclude = ('id',)
