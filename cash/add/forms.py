from django import forms

class Bankacc(forms.Form):
    u_name    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'User Name'
            }
        )
    )

    f_name    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'First Name'
            }
        )
    )

    l_name    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'Last Name'
            }
        )
    )

    birthday    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'birthday (mmddyy)'
            }
        )
    )

    allmoney    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'Fund'
            }
        )
    )



    