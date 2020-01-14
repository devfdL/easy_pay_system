from django import forms

class dataqr(forms.Form):
    data    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'',
                'placeholder':'QR Data'
            }
        )
    )

    



    