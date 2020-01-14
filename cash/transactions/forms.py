from django import forms
from django.forms import formset_factory

class pay(forms.Form):
    sender    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'User Name'
            }
        )
    )

    place    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'place'
            }
        )
    )


    nominal    = forms.CharField(
        max_length=50,
        label = '',
         widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'nominal'
            }
        )
    )

    date    = forms.CharField(
        max_length=50,
        label = '',
         widget = forms.TextInput(
            attrs={
                'class':'chat-control',
                'placeholder':'date'
            }
        )
    )


class bill(forms.Form):

    price    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'price-control',
                'placeholder':'total price'
            }
        )
    )


