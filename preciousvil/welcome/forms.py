#welcome/forms.py
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = (
            'name','corporate','phone_number','email','address','type_set','detail',
        )
        widgets = {
            'type_set' : forms.CheckboxSelectMultiple()
        }
'''
        def save(self, commit=True):
            reservation = Reservation(**form.cleaned_data)
            if commit:
                                                                                                                                                                                                                                                                                                                                                                                                                 reservation.save()
            return reservation
'''

class SecretForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields =('phone_number',)