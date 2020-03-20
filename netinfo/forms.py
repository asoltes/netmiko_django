from django import forms

class CmdForm(forms.Form):
        command = forms.CharField(label='Command to execute')