from django import forms

class CartAddForm(forms.Form) :
    number = forms.IntegerField(min_value=1, initial='1', max_value=9, label='تعداد')